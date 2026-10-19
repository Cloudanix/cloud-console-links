# AGENTS.md

This file provides guidance to Agents when working with code in this repository.

## What this is

`cloudconsolelink` is a pure-Python library (no runtime deps) that turns a cloud resource identifier into a deep-link into the AWS, Azure, GCP, or OCI (Oracle) web console, plus container-image links for ECR, GAR/GCR, ACR, Docker Hub, and OCIR. Published to PyPI; used by Cloudanix.

```python
from cloudconsolelink.clouds.aws      import AWSLinker           # .get_console_link(arn=...)
from cloudconsolelink.clouds.azure    import AzureLinker         # .get_console_link(id=..., iam_entity_type=... | primary_ad_domain_name=...)
from cloudconsolelink.clouds.gcp      import GCPLinker           # .get_console_link(resource_name=..., **params)
from cloudconsolelink.clouds.oci      import OCILinker           # .get_console_link(resource_name=..., **kwargs)
from cloudconsolelink.clouds.registry import image_console_link  # image_console_link("host/repo[:tag][@digest]", **hints)
```

## Commands

```bash
pip install -e '.[dev]'          # dev extras = requirements-dev.txt (CI uses `uv pip install -e '.[dev]'`)

make test                        # pytest tests -q
make coverage                    # with coverage (setup.cfg: fail_under = 30)
make test-arn                    # AWS ARN-template contract tests only
make test-aws-links              # a few AWS link smoke tests
make check                       # test + coverage

pytest tests/test_gcp.py -k storage_bucket    # single test
pre-commit run --all-files                    # lint/format/typecheck: ruff (line 120), mypy, pyupgrade, reorder-python-imports, autoflake
```

pre-commit excludes `tests/`. CI (`.github/workflows/code-quality.yaml`) runs pre-commit + `make coverage` on PRs to `develop`.

## Versioning and release

- `setup.py` takes the version from `git describe --tags`; `__version__` in `cloudconsolelink/__init__.py` is only the fallback when no git/tags (e.g. building from an sdist). Don't bump `__version__` to release.
- Push to `main` triggers `release.yml`: computes next semver tag from labels on PRs merged since the last tag (`major` / `minor` label, else patch) and creates a GitHub release.

## Architecture: per-provider dispatch

Every provider maps an identifier to a URL template; identifier and lookup differ. Returned links have spaces stripped (`.replace(" ", "")`) because templates are written as multi-line strings.

**AWS: ARN-driven** (`clouds/aws/__init__.py` + `links.py`)
- `get_console_link(arn)` splits `prefix:partition:service:region:account:resource...`, then looks up `get_links()[service][resourceType]` in `links.py` (large nested dict). API Gateway ARNs with a leading `/` in the resource are handled as path-style.
- Templates are rendered by `_render()` **without eval**: each `{expr}` (whitespace collapsed) is looked up in a fixed context dict (`data.get("region","")`, `data.get("resource","")`, `get_arn_string(data)`, `get_resource_path(...)`, `arn`, etc.). An expression not in that dict silently renders `""`, so new templates must use only those exact expressions, or extend the dict.
- `HOME_URLS` (top of `links.py`) overrides service home only where it differs from `https://{region}.console.aws.amazon.com/{service}/home?region={region}`.
- No resource tokens or unsupported `resourceType` returns the service home link instead of raising. A `None` template marks a retired service.
- Errors in `clouds/aws/errors.py`, all subclassing `AWSLinkerError(ValueError)`. Partitions: `aws`, `aws-us-gov`, `aws-cn` (see `get_console`).

**GCP / OCI: resource_name-driven** (`clouds/gcp/links.py`, `clouds/oci/links.py`)
- `Resource` class has one method per resource type (`storage_bucket`, `compute_instance`, ...).
- `SERVICE_HOME_MAP` in each `links.py`: unknown `resource_name` falls back to a mapped `*_home` method instead of raising.
- GCP declares every param explicitly: `build_kwargs` + the long keyword list on `GCPLinker.get_console_link` + a `resources` dict registering each method. OCI uses `**kwargs` and `getattr(resource, resource_name)`.

**Azure: id-driven** (`clouds/azure/__init__.py`, no `links.py`)
- Templates inline in `get_console_link`. IAM entities use `iam_entity_type`; management resources use the raw resource `id` + `primary_ad_domain_name`.

**Registry: hostname-driven** (`clouds/registry/__init__.py`, design in `docs/oci-images/spec.md`; "OCI" there means Open Container Initiative, not Oracle)
- `parse_image_ref` -> `ImageRef(host, repository, tag, digest)`; `classify(host)` -> family key; `_BUILDERS[family]` builds the link.
- Repo-level links delegate to `AWSLinker` / `GCPLinker` rather than duplicating URLs; only image/digest drill-ins and providers without a linker (Docker Hub, ECR Public, OCIR, ACR) build URLs directly. ACR needs `subscription_id` + `resource_group` hints, else falls back to a browse page. Unknown host falls back to Docker Hub search.

## Adding a resource

- **AWS**: add `service -> resourceType -> template` to `get_links()` in `links.py` (plus `HOME_URLS` if home is non-standard). Run `make test-arn`.
- **GCP**: add a `Resource` method, register it in the `resources` dict in `clouds/gcp/__init__.py`, add any new param to both `build_kwargs` and `get_console_link`, and add a sample value to `GCP_SAMPLE_ARGS` in `tests/test_provider_coverage.py`.
- **OCI**: add a `Resource` method (auto-dispatched); add sample args to `OCI_SAMPLE_ARGS` if it needs new params.

`tests/test_provider_coverage.py` is a coverage contract: it reflects over every `Resource` method and AWS ARN template shape and asserts each is reachable, returns a console URL, and validates required params. A resource not wired in correctly fails there.
