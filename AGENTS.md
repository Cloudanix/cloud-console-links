# AGENTS.md

This file provides guidance to Agents when working with code in this repository.

## What this is

`cloudconsolelink` is a pure-Python library (no runtime deps) that generates deep-links into the AWS, Azure, GCP, and OCI web consoles for a given cloud resource. Published to PyPI; used by Cloudanix.

Public entry points, one linker per provider:

```python
from cloudconsolelink.clouds.aws   import AWSLinker    # .get_console_link(arn=...)
from cloudconsolelink.clouds.azure import AzureLinker  # .get_console_link(id=..., iam_entity_type=... | primary_ad_domain_name=...)
from cloudconsolelink.clouds.gcp   import GCPLinker    # .get_console_link(resource_name=..., **params)
from cloudconsolelink.clouds.oci   import OCILinker    # .get_console_link(resource_name=..., **kwargs)
```

## Commands

```bash
pip install -e '.[dev]'      # local setup (dev extras = requirements-dev.txt)

make test                    # pytest tests -q
make coverage                # + coverage report (setup.cfg: fail_under = 30)
make test-arn                # AWS ARN-template coverage contract tests only
make test-aws-links          # a few AWS link smoke tests
make check                   # test + coverage

pytest tests/test_gcp.py -k cloud_spanner_database   # run a single test
flake8 cloudconsolelink                              # max-line-length = 120
```

Version lives in `cloudconsolelink/__init__.py` (`__version__`); `setup.py` reads it via `exec`.

## Architecture — three dispatch styles

Each provider maps a resource identifier to a URL template, but the identifier and lookup differ. Every returned link is passed through `.replace(" ", "")` because templates are written as multi-line strings for readability.

**AWS — ARN-driven** (`clouds/aws/__init__.py` + `links.py`):
- `get_console_link(arn)` splits the ARN into `prefix:partition:service:region:account:resource…`, then looks up `get_links()[service][resourceType]` — a giant nested dict in `links.py` (~1200 lines) keyed by AWS service then resource type.
- Templates are **f-string-like strings eval'd by `_render()`** against `{"data": data, "arn": arn}`. Write them with `{data.get("region", "")}`, `{data.get("resource", "")}`, `{arn}` placeholders. An unknown expression renders to `""` (see `_render` / `_sub`).
- `HOME_URLS` (top of `links.py`) overrides the console home only for services whose home URL doesn't match the default `https://{region}.console.aws.amazon.com/{service}/home?region={region}` pattern.
- Fallbacks: no resource tokens, or an unsupported `resourceType`, returns the **service home link** rather than raising. A `None` template value marks a retired service.
- Errors are typed in `clouds/aws/errors.py` — all subclass `AWSLinkerError(ValueError)`: `ARNTooShortError`, `InvalidARNError`, `InvalidPartitionError`, `InvalidServiceError`. Valid partitions: `aws`, `aws-us-gov`, `aws-cn`.

**GCP / OCI — resource_name-driven** (`clouds/gcp/links.py`, `clouds/oci/links.py`):
- A `Resource` class holds **one method per resource type** (`storage_bucket`, `compute_instance`, …). `get_console_link(resource_name=...)` dispatches to `resource.<resource_name>(**params)`.
- `SERVICE_HOME_MAP` in each `links.py` gives a fallback: an unknown `resource_name` falls back to the mapped `*_home` method instead of raising.
- GCP declares every param explicitly (`build_kwargs` + a long keyword list on `get_console_link`) — adding a param means touching both. OCI is leaner: `**kwargs` + `getattr(resource, resource_name)` dispatch.

**Azure — id-driven** (`clouds/azure/__init__.py`, no `links.py`):
- Templates are inline dicts inside `get_console_link`. IAM entities (`user`/`group`/`application`/`role`/`service_principal`/`domain`) use `iam_entity_type`; management resources use `primary_ad_domain_name` and the raw resource `id`.

## Adding a resource

- **AWS**: add a `service → resourceType → template` entry in `get_links()` in `links.py` (and `HOME_URLS` if its console home is non-standard).
- **GCP**: add a method to `Resource`, register it in the `resources` dict in `clouds/gcp/__init__.py`, and add any new param to both `build_kwargs` and `get_console_link`.
- **OCI**: add a method to `Resource` (auto-dispatched by name).

`tests/test_provider_coverage.py` is a **coverage contract**: it reflects over `Resource` methods and AWS ARN template shapes and asserts each is reachable/exercised. A new resource that isn't wired in correctly will fail these tests — run `make test-arn` after AWS changes.


## Token Efficiency (MANDATORY)

Token optimization is not optional. Use every tool below on every session.

### Setup — Install All Tools

Check and install once per machine:

```bash
# 1. caveman — terse communication style plugin
claude plugin install caveman@caveman

# 2. code-review-graph — structural code knowledge graph
pip install code-review-graph
code-review-graph --version   # verify: code-review-graph X.Y.Z
# then build the graph for this repo:
code-review-graph build .
```

lean-ctx (the `ctx_*` context runtime) is configured globally — see the lean-ctx section in `~/.claude/CLAUDE.md`; it auto-installs on demand. After install, restart Claude Code to activate plugins.

### Communication Style — Caveman Mode

Respond terse. Drop: articles (a/an/the), filler (just/really/basically/actually), pleasantries (sure/certainly/happy to), hedging. Fragments OK. Short synonyms (fix not "implement a solution for"). Technical terms exact. Code blocks unchanged.

Auto-expand ONLY for: security warnings, irreversible action confirmations, user confusion.

### lean-ctx — Context Window Protection

Raw tool output floods context. Prefer the `ctx_*` tools over native equivalents — full config + tool list live in the lean-ctx section of `~/.claude/CLAUDE.md`. Shadow mode auto-routes native file/search/shell calls to `ctx_*`, so most of this is transparent; only the printed summary enters context.

| Native | Use instead | Why |
|--------|-------------|-----|
| Read / cat | `ctx_read` | Cached, re-reads ~13 tokens; modes: full / map / signatures / lines:N-M |
| Grep / rg | `ctx_search` | Compact results |
| Bash / Shell | `ctx_shell` | 95+ compression patterns; also the reliable path when plain Bash trips the eval-wrapping sandbox guard |
| ls / find | `ctx_tree` | Compact directory maps |
| — | `ctx_compose` | Orient FIRST — bundles search + read + symbols in one call |

Native Edit/Write stay unchanged; if Edit is denied by a Read deny rule, use `ctx_patch`.

### MCP Tools: code-review-graph

**ALWAYS use code-review-graph tools BEFORE Grep/Glob/Read.** Faster, cheaper, gives structural context (callers, dependents, test coverage).

| Tool | Use when |
|------|----------|
| `detect_changes` | Code review — risk-scored analysis |
| `get_review_context` | Source snippets — token-efficient |
| `get_impact_radius` | Blast radius of a change |
| `get_affected_flows` | Impacted execution paths |
| `query_graph` | Trace callers/callees/imports/tests |
| `semantic_search_nodes` | Find functions/classes by name/keyword |
| `get_architecture_overview` | High-level structure |
| `refactor_tool` | Renames, dead code |

Fallback to Grep/Glob/Read only when graph insufficient. Graph auto-updates on file changes.
