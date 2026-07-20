# Design: Container Registry (OCI Image) Deep Links

Add console deep-links for container **registries and images** (ECR, GAR/GCR,
ACR, Docker Hub, OCI Registry) to `cloudconsolelink`.

> "OCI" in this doc's path = Open Container Initiative image references, **not**
> Oracle Cloud Infrastructure (which this library also supports under
> `clouds/oci`). The two are unrelated.

Motivating example:

```
602401143452.dkr.ecr.us-east-2.amazonaws.com/amazon-k8s-cni-init
```

should resolve to the ECR repository `amazon-k8s-cni-init` in account
`602401143452`, region `us-east-2`, and (when a tag/digest is present) to that
specific image.

---

## 1. Current link-generation architecture

Every provider maps a resource identifier to a URL template, but the *identifier*
and the *lookup* differ. Four dispatch styles exist today (see `AGENTS.md`):

| Provider | Entry point | Identifier | Dispatch |
|----------|-------------|------------|----------|
| AWS | `AWSLinker.get_console_link(arn=...)` | ARN | split ARN → `get_links()[service][resourceType]` nested dict, rendered by `_render()` (`clouds/aws/__init__.py`, `links.py`) |
| GCP | `GCPLinker.get_console_link(resource_name=..., **params)` | `resource_name` + explicit kwargs | `getattr(resource, resource_name)(**params)` on a `Resource` class (`clouds/gcp/links.py`) |
| OCI | `OCILinker.get_console_link(resource_name=..., **kwargs)` | `resource_name` + `**kwargs` | `getattr(resource, resource_name)(**kwargs)` (`clouds/oci/links.py`) |
| Azure | `AzureLinker.get_console_link(id=..., iam_entity_type=...)` | resource `id` | inline template dicts (`clouds/azure/__init__.py`) |

Common invariant: the returned URL is passed through `.replace(" ", "")` because
templates are multi-line strings.

**What already exists for registries:**

- AWS `ecr` service has `repository` and `image` templates
  (`links.py:410-415`), fired by an **ARN**
  (`arn:aws:ecr:<region>:<account>:repository/<name>`). Both currently point at the
  repository; neither drills into a tag/digest. The URL form is the older
  `/ecr/repositories/<repo>` (no `/private/<account>/`).
- GCP `artifact_registry_repository` (`links.py:681`) needs
  `project_id` + `region` + `instance_name` kwargs; repo-level, no image segment.
- OCI `container_repository` (`links.py:233`) needs `region` + `ocid`.
- Azure ACR: nothing.
- Docker Hub: nothing.

### Why image references don't fit any existing entry point

A container image reference is a **registry hostname + repository path**, e.g.
`602401143452.dkr.ecr.us-east-2.amazonaws.com/amazon-k8s-cni-init:v1.2`. It is
**not** an ARN, GCP/OCI `resource_name`, or Azure `id`. But the *hostname
self-identifies the provider* — parse it and you know provider, region,
account/project, and repo. That is a new identifier axis, so it gets a thin front
door.

---

## 2. Proposed design — adapter, not a parallel linker

Key decision: **do not** build a second set of per-registry URL builders. An ECR
image *is* an AWS resource; a GAR image *is* a GCP resource. The existing linkers
already own those URL templates. Duplicating them means two places to fix when a
console URL changes.

Instead, the front door **normalizes an image ref into an existing identifier and
delegates** to the existing linker. New URL-building code exists *only* for
registries with no existing path (Docker Hub, ECR Public, ACR).

```
image_ref ──parse──▶ {host, repository, tag, digest}
                        │
                   classify(host)
                        │
   ┌──────────── delegate to existing linker ────────────┐   ┌─ new builders ─┐
  ECR                  GAR/GCR              OCI-Registry     Docker Hub / ECR-Public / ACR
   │                    │                     │                     │
 build ARN         build resource_name    build OCI path     (self-contained URL)
 → AWSLinker        + params → GCPLinker   → OCILinker              │
   └────────────────────────┬──────────────────────┘               │
                            console URL ◀───────────────────────────┘
```

### 2.1 Entry point

```python
from cloudconsolelink.clouds.registry import image_console_link

image_console_link(
    "602401143452.dkr.ecr.us-east-2.amazonaws.com/amazon-k8s-cni-init:v1.2",
    # optional hints for registries whose console URL needs data absent from the ref:
    subscription_id=..., resource_group=...,   # ACR only
)
```

A module-level function (or a thin `ContainerRegistryLinker` wrapper for symmetry
with the other `*Linker` classes — pick one; the function is enough). It is a
router, not a linker: it constructs an identifier and calls the real linker.

### 2.2 Parse

Reference grammar (OCI distribution spec):

```
[registry-host[:port]/]repository[:tag][@digest]
```

- No host, or host without `.`/`:` and not `localhost` → Docker Hub.
- `repository` may hold multiple `/` segments (namespace/repo, project/repo/image…).

`parse_image_ref(ref) -> ImageRef` (small namedtuple `{host, repository, tag,
digest}`, no runtime deps).

### 2.3 Classify (regex per host family)

| Registry | Host pattern | Route |
|----------|--------------|-------|
| ECR private | `<account>.dkr.ecr.<region>.amazonaws.com[.cn]` | **delegate → AWSLinker** |
| GAR | `<location>-docker.pkg.dev` | **delegate → GCPLinker** |
| GCR legacy | `gcr.io`, `<us\|eu\|asia>.gcr.io` | **delegate → GCPLinker** |
| OCI Registry | `<region>.ocir.io` | **delegate → OCILinker** |
| ECR Public | `public.ecr.aws` | new builder |
| ACR | `<registry>.azurecr.io` | new builder (+hints) |
| Docker Hub | `docker.io`, `registry-1.docker.io`, bare | new builder |

### 2.4 Delegation (reuse existing templates)

**ECR private.** Host → account + region; path → repo.
```python
arn = f"arn:{partition}:ecr:{region}:{account}:repository/{repository}"
AWSLinker().get_console_link(arn=arn)
```
Partition derived from the host suffix (`.amazonaws.com.cn` → `aws-cn`). Gives the
repo link today via the existing `ecr/repository` template.

**GAR.** `<loc>-docker.pkg.dev/<project>/<repo>/<image>` →
```python
GCPLinker().get_console_link(
    resource_name="artifact_registry_repository",
    project_id=project, region=loc, instance_name=repo,
)
```

**GCR / OCI Registry.** Same pattern against their existing `Resource` methods.

### 2.5 Tag / digest drill-in — extend templates in place

The existing templates are repo-level. To reach a specific image, **extend the
existing templates**, do not fork them:

- ECR: `image` template →
  `…/ecr/repositories/private/<account>/<repo>/_/image/<digest>/details?region=<region>`
  when a digest is present. (Also modernizes the repo template to the canonical
  `/private/<account>/` form.) ECR console addresses images by **digest**; a
  tag-only ref stays at the repo view (tags are listed there) — documented limit.
- GAR: append the image segment to the Artifact Registry template.

These edits live in `links.py` next to the current templates, so there is still one
source of truth per provider.

### 2.6 New builders (no existing path)

- **Docker Hub.**
  `docker.io/<ns>/<repo>[:tag]` → `https://hub.docker.com/r/<ns>/<repo>[/tags?name=<tag>]`;
  `library/<repo>` → `https://hub.docker.com/_/<repo>` (official).
- **ECR Public.** `public.ecr.aws/<alias>/<repo>` → `https://gallery.ecr.aws/<alias>/<repo>`.
- **ACR.** Portal blade needs the ARM id
  `/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.ContainerRegistry/registries/<name>`.
  `<sub>`/`<rg>` are **not** in `<name>.azurecr.io/<repo>`:
  - with `subscription_id`+`resource_group` hints → full RepositoryBlade deep-link;
  - without → registry-browse fallback
    (`…/BrowseResource/resourceType/Microsoft.ContainerRegistry%2Fregistries`).

  `ponytail:` no cloud-API lookup to recover sub/RG — take the optional hints,
  degrade to browse otherwise. Add lookup only if a consumer needs the deep blade
  without hints.

### 2.7 Return contract

Return the console URL string. Unrecognized host → fallback (Docker Hub search /
registry root), matching AWS's "unknown resource → service home" behavior. Reserve
exceptions for malformed refs.

---

## 3. API surface

```python
# cloudconsolelink/clouds/registry/__init__.py
def image_console_link(image_ref: str, **hints) -> str: ...

# module-private
def parse_image_ref(ref: str) -> ImageRef: ...   # {host, repository, tag, digest}
def classify(host: str) -> str: ...              # "ecr" | "ecr-public" | "gar" | "gcr" | "ocir" | "acr" | "dockerhub" | ""
```

No new runtime deps (library constraint). Delegation targets are the existing
`AWSLinker` / `GCPLinker` / `OCILinker`.

---

## 4. Wiring & tests

- New package `cloudconsolelink/clouds/registry/` (parser + classifier + router;
  new builders inline until they grow).
- Template edits for ECR/GAR image drill-in go in the respective `links.py`.
- Extend `tests/test_provider_coverage.py` (the coverage contract) with a
  registry-family list asserting each classifier → route is reachable.
- Table-driven `(image_ref, expected_url)` tests: motivating ECR example, tag vs
  digest, nested repos, ECR Public, GAR, GCR legacy, OCI Registry, Docker Hub
  official (`library/*`), ACR with/without hints.
- `parse_image_ref` unit tests: bare name → Docker Hub, host with port, tag+digest
  together, multi-segment repository.

---

## 5. Suggested phasing

Each phase independently shippable; router returns a fallback for
not-yet-wired families.

1. **Parser + classifier + ECR delegation** (private & public). Covers the
   motivating case; ECR image drill-in template edit.
2. **GAR + GCR delegation.** Reuses/extends the Artifact Registry template.
3. **Docker Hub.** Pure string mapping.
4. **OCI Registry delegation + ACR** (with optional hints + browse fallback).
