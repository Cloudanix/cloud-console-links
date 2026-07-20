"""Container-registry (OCI image) console deep-links.

An image reference (``registry-host/repository[:tag][@digest]``) is a different
identifier axis than an ARN / resource_name / resource id: the *hostname*
identifies the provider. This module parses the reference, classifies the host,
and routes to a console link — delegating to the existing provider linkers where
a path already exists, and building the URL directly only where none does
(Docker Hub, ECR Public, GCR, OCIR, ACR, and image/digest drill-in).

See ``docs/oci-images/spec.md``.
"""
import re
from collections import namedtuple
from urllib.parse import quote

from cloudconsolelink.clouds.aws import AWSLinker, get_console
from cloudconsolelink.clouds.gcp import GCPLinker

ImageRef = namedtuple("ImageRef", ["host", "repository", "tag", "digest"])

# <account>.dkr.ecr.<region>.amazonaws.com  (optional .cn for the aws-cn partition)
_ECR_HOST = re.compile(r"^(\d+)\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?$")
# <region>.gcr.io legacy hosts (gcr.io, us.gcr.io, eu.gcr.io, asia.gcr.io, ...)
_GCR_HOST = re.compile(r"^([a-z0-9-]+\.)?gcr\.io$")

_DOCKERHUB_HOSTS = {"", "docker.io", "registry-1.docker.io", "index.docker.io"}


def parse_image_ref(ref):
    """Split an OCI image reference into ``ImageRef(host, repository, tag, digest)``.

    Grammar: ``[registry-host[:port]/]repository[:tag][@digest]``. A first path
    segment that looks like a hostname (contains ``.`` or ``:``, or is
    ``localhost``) is treated as the registry host; otherwise the reference is
    hostless (Docker Hub). ``repository`` keeps all remaining ``/`` segments.
    """
    ref = (ref or "").strip()
    if not ref:
        raise ValueError("empty image reference")

    digest = ""
    if "@" in ref:
        ref, digest = ref.split("@", 1)

    first, slash, rest = ref.partition("/")
    if slash and ("." in first or ":" in first or first == "localhost"):
        host, path = first, rest
    else:
        host, path = "", ref

    tag = ""
    seg_start = path.rfind("/") + 1
    colon = path.find(":", seg_start)
    if colon != -1:
        tag = path[colon + 1:]
        path = path[:colon]

    if not path:
        raise ValueError(f"image reference has no repository: {ref!r}")

    return ImageRef(host=host, repository=path, tag=tag, digest=digest)


def classify(host):
    """Map a registry hostname to a registry family key.

    Returns one of ``ecr`` | ``ecr-public`` | ``gar`` | ``gcr`` | ``ocir`` |
    ``acr`` | ``dockerhub``, or ``""`` for an unrecognized host.
    """
    if host in _DOCKERHUB_HOSTS:
        return "dockerhub"
    if host == "public.ecr.aws":
        return "ecr-public"
    if _ECR_HOST.match(host):
        return "ecr"
    if host.endswith("-docker.pkg.dev"):
        return "gar"
    if _GCR_HOST.match(host):
        return "gcr"
    if host.endswith(".ocir.io"):
        return "ocir"
    if host.endswith(".azurecr.io"):
        return "acr"
    return ""


# --- per-family builders ---------------------------------------------------
# Repo-level links delegate to the existing provider linker (no URL duplicated).
# Image/tag/digest drill-in URLs are built here because no existing identifier
# (ARN / resource_name) can carry image coordinates.


def _ecr(ref, hints):
    account, region, cn = _ECR_HOST.match(ref.host).groups()
    if region.startswith("us-gov-"):
        partition = "aws-us-gov"
    elif cn:
        partition = "aws-cn"
    else:
        partition = "aws"

    if ref.digest:
        # ECR console addresses images by digest — net-new, ARN can't carry it.
        console = get_console(partition)
        return (
            f"https://{region}.{console}/ecr/repositories/private/{account}/"
            f"{ref.repository}/_/image/{ref.digest}/details?region={region}"
        )

    # Repo view (tag-only refs land here too — tags are listed on the repo page).
    arn = f"arn:{partition}:ecr:{region}:{account}:repository/{ref.repository}"
    return AWSLinker().get_console_link(arn=arn)


def _ecr_public(ref, hints):
    return f"https://gallery.ecr.aws/{ref.repository}"


def _gar(ref, hints):
    location = ref.host[: -len("-docker.pkg.dev")]
    parts = ref.repository.split("/")
    project, repo = parts[0], parts[1] if len(parts) > 1 else ""

    if len(parts) >= 3:
        image = "/".join(parts[2:])  # net-new: image drill-in below the repo
        return (
            f"https://console.cloud.google.com/artifacts/docker/{project}/{location}/"
            f"{repo}/{image}?project={project}"
        )

    # project/repo -> repo view via the existing Artifact Registry template.
    return GCPLinker().get_console_link(
        resource_name="artifact_registry_repository",
        project_id=project,
        region=location,
        instance_name=repo,
    )


def _gcr(ref, hints):
    # gcr.io -> GLOBAL, us.gcr.io -> US, eu.gcr.io -> EU, asia.gcr.io -> ASIA
    prefix = ref.host[: -len(".gcr.io")] if ref.host != "gcr.io" else ""
    location = prefix.upper() if prefix else "GLOBAL"
    parts = ref.repository.split("/")
    project = parts[0]
    image = "/".join(parts[1:])
    if not image:
        return f"https://console.cloud.google.com/gcr/images/{project}?project={project}"
    return (
        f"https://console.cloud.google.com/gcr/images/{project}/{location}/"
        f"{image}?project={project}"
    )


def _dockerhub(ref, hints):
    parts = ref.repository.split("/")
    if len(parts) == 1:
        namespace, repo = "library", parts[0]
    else:
        namespace, repo = parts[0], "/".join(parts[1:])

    if namespace == "library":
        url = f"https://hub.docker.com/_/{repo}"
    else:
        url = f"https://hub.docker.com/r/{namespace}/{repo}"
    if ref.tag:
        url += f"/tags?name={ref.tag}"
    return url


def _ocir(ref, hints):
    # OCIR console needs an OCID (absent from the image ref) to reach a repo, so
    # fall back to the Container Registry landing page. ponytail: no OCID lookup.
    return "https://cloud.oracle.com/registry/containers/repos"


def _acr(ref, hints):
    name = ref.host[: -len(".azurecr.io")]
    sub = hints.get("subscription_id")
    rg = hints.get("resource_group")
    if sub and rg:
        arm_id = (
            f"/subscriptions/{sub}/resourceGroups/{rg}/providers/"
            f"Microsoft.ContainerRegistry/registries/{name}"
        )
        return (
            "https://portal.azure.com/#view/Microsoft_Azure_ContainerRegistries/"
            f"RepositoryBlade/registryId/{quote(arm_id, safe='')}/repository/{ref.repository}"
        )
    # No subscription/resource-group hints -> registry browse fallback.
    return (
        "https://portal.azure.com/#blade/HubsExtension/BrowseResource/"
        "resourceType/Microsoft.ContainerRegistry%2Fregistries"
    )


_BUILDERS = {
    "ecr": _ecr,
    "ecr-public": _ecr_public,
    "gar": _gar,
    "gcr": _gcr,
    "dockerhub": _dockerhub,
    "ocir": _ocir,
    "acr": _acr,
}


def image_console_link(image_ref, **hints):
    """Return a cloud-console deep-link for a container image reference.

    ``hints`` supplies data absent from the reference itself — currently
    ``subscription_id`` and ``resource_group`` for Azure Container Registry.
    An unrecognized registry host falls back to a Docker Hub search.
    """
    ref = parse_image_ref(image_ref)
    builder = _BUILDERS.get(classify(ref.host))
    if builder is None:
        return f"https://hub.docker.com/search?q={quote(ref.repository)}"
    return builder(ref, hints)


__all__ = ["ImageRef", "parse_image_ref", "classify", "image_console_link"]
