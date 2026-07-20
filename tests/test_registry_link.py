from urllib.parse import quote

import pytest

from cloudconsolelink.clouds.registry import image_console_link


@pytest.mark.parametrize(
    "ref, expected",
    [
        # --- ECR private (delegates to AWSLinker via a reconstructed ARN) ---
        (
            "602401143452.dkr.ecr.us-east-2.amazonaws.com/amazon-k8s-cni-init",
            "https://us-east-2.console.aws.amazon.com/ecr/repositories/private/"
            "602401143452/amazon-k8s-cni-init?region=us-east-2",
        ),
        # digest drill-in (built directly, ARN cannot carry a digest)
        (
            "602401143452.dkr.ecr.us-east-2.amazonaws.com/repo@sha256:abc123",
            "https://us-east-2.console.aws.amazon.com/ecr/repositories/private/"
            "602401143452/repo/_/image/sha256:abc123/details?region=us-east-2",
        ),
        # tag-only lands on the repo view
        (
            "602401143452.dkr.ecr.us-east-2.amazonaws.com/repo:v1",
            "https://us-east-2.console.aws.amazon.com/ecr/repositories/private/"
            "602401143452/repo?region=us-east-2",
        ),
        # China partition
        (
            "123456789012.dkr.ecr.cn-north-1.amazonaws.com.cn/repo",
            "https://cn-north-1.console.amazonaws.cn/ecr/repositories/private/"
            "123456789012/repo?region=cn-north-1",
        ),
        # GovCloud partition (detected from the region prefix)
        (
            "123456789012.dkr.ecr.us-gov-west-1.amazonaws.com/repo",
            "https://us-gov-west-1.console.amazonaws-us-gov.com/ecr/repositories/private/"
            "123456789012/repo?region=us-gov-west-1",
        ),
        # --- ECR Public ---
        ("public.ecr.aws/nginx/nginx", "https://gallery.ecr.aws/nginx/nginx"),
        # --- GAR: image drill-in vs repo-only delegation ---
        (
            "us-docker.pkg.dev/proj/repo/img",
            "https://console.cloud.google.com/artifacts/docker/proj/us/repo/img?project=proj",
        ),
        (
            "europe-west1-docker.pkg.dev/proj/repo",
            "https://console.cloud.google.com/artifacts/docker/proj/europe-west1/repo?project=proj",
        ),
        # --- GCR legacy ---
        (
            "gcr.io/proj/img",
            "https://console.cloud.google.com/gcr/images/proj/GLOBAL/img?project=proj",
        ),
        (
            "us.gcr.io/proj/img",
            "https://console.cloud.google.com/gcr/images/proj/US/img?project=proj",
        ),
        (
            "gcr.io/proj",
            "https://console.cloud.google.com/gcr/images/proj?project=proj",
        ),
        # --- Docker Hub ---
        ("nginx", "https://hub.docker.com/_/nginx"),
        ("library/nginx", "https://hub.docker.com/_/nginx"),
        ("nginx:1.25", "https://hub.docker.com/_/nginx/tags?name=1.25"),
        ("bitnami/nginx", "https://hub.docker.com/r/bitnami/nginx"),
        ("bitnami/nginx:1.25", "https://hub.docker.com/r/bitnami/nginx/tags?name=1.25"),
        # --- OCIR (no OCID in ref -> registry landing page) ---
        ("iad.ocir.io/tenancy/repo", "https://cloud.oracle.com/registry/containers/repos"),
        # --- unknown registry -> Docker Hub search fallback ---
        ("quay.io/org/app", "https://hub.docker.com/search?q=org/app"),
    ],
)
def test_image_console_link(ref, expected):
    assert image_console_link(ref) == expected


def test_acr_with_hints():
    url = image_console_link(
        "myreg.azurecr.io/app",
        subscription_id="SUB",
        resource_group="RG",
    )
    arm_id = "/subscriptions/SUB/resourceGroups/RG/providers/Microsoft.ContainerRegistry/registries/myreg"
    expected = (
        "https://portal.azure.com/#view/Microsoft_Azure_ContainerRegistries/"
        f"RepositoryBlade/registryId/{quote(arm_id, safe='')}/repository/app"
    )
    assert url == expected


def test_acr_without_hints_browse_fallback():
    url = image_console_link("myreg.azurecr.io/app")
    assert url == (
        "https://portal.azure.com/#blade/HubsExtension/BrowseResource/"
        "resourceType/Microsoft.ContainerRegistry%2Fregistries"
    )


def test_acr_partial_hints_falls_back():
    # only one of the two required hints -> still the browse fallback
    url = image_console_link("myreg.azurecr.io/app", subscription_id="SUB")
    assert "BrowseResource" in url


def test_invalid_ref_raises():
    with pytest.raises(ValueError):
        image_console_link("")


def test_gar_single_segment_raises_clear_error():
    with pytest.raises(ValueError, match="GAR image reference needs"):
        image_console_link("us-docker.pkg.dev/proj")
