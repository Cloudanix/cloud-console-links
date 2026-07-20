"""Container-registry (OCI image) console deep-links.

An image reference (``registry-host/repository[:tag][@digest]``) is a different
identifier axis than an ARN / resource_name / resource id: the *hostname*
identifies the provider. This module parses the reference, classifies the host,
and routes to a console link — delegating to the existing provider linkers where
a path already exists (see ``image_console_link``).

See ``docs/oci-images/spec.md``.
"""
import re
from collections import namedtuple

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


__all__ = ["ImageRef", "parse_image_ref", "classify"]
