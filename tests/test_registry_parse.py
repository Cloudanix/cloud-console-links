import pytest

from cloudconsolelink.clouds.registry import ImageRef, classify, parse_image_ref


@pytest.mark.parametrize(
    "ref, expected",
    [
        # bare name -> Docker Hub, no host
        ("nginx", ImageRef("", "nginx", "", "")),
        ("nginx:1.25", ImageRef("", "nginx", "1.25", "")),
        ("library/nginx", ImageRef("", "library/nginx", "", "")),
        # explicit docker.io host
        ("docker.io/library/nginx:latest", ImageRef("docker.io", "library/nginx", "latest", "")),
        # ECR private, the motivating example
        (
            "602401143452.dkr.ecr.us-east-2.amazonaws.com/amazon-k8s-cni-init",
            ImageRef("602401143452.dkr.ecr.us-east-2.amazonaws.com", "amazon-k8s-cni-init", "", ""),
        ),
        # tag + digest together
        (
            "reg.example.com/team/app:v1@sha256:abcdef",
            ImageRef("reg.example.com", "team/app", "v1", "sha256:abcdef"),
        ),
        # digest only
        (
            "602401143452.dkr.ecr.us-east-2.amazonaws.com/repo@sha256:deadbeef",
            ImageRef("602401143452.dkr.ecr.us-east-2.amazonaws.com", "repo", "", "sha256:deadbeef"),
        ),
        # host with port
        ("localhost:5000/my/img:dev", ImageRef("localhost:5000", "my/img", "dev", "")),
        ("localhost/img", ImageRef("localhost", "img", "", "")),
        # multi-segment repository (GAR: project/repo/image)
        (
            "us-docker.pkg.dev/proj/repo/img:tag",
            ImageRef("us-docker.pkg.dev", "proj/repo/img", "tag", ""),
        ),
        # surrounding whitespace stripped
        ("  nginx:1  ", ImageRef("", "nginx", "1", "")),
    ],
)
def test_parse_image_ref(ref, expected):
    assert parse_image_ref(ref) == expected


@pytest.mark.parametrize("bad", ["", "   ", None])
def test_parse_image_ref_empty_raises(bad):
    with pytest.raises(ValueError):
        parse_image_ref(bad)


def test_parse_image_ref_host_only_no_repo_raises():
    # host present but nothing after the slash
    with pytest.raises(ValueError):
        parse_image_ref("reg.example.com/")


@pytest.mark.parametrize(
    "host, family",
    [
        ("", "dockerhub"),
        ("docker.io", "dockerhub"),
        ("registry-1.docker.io", "dockerhub"),
        ("index.docker.io", "dockerhub"),
        ("public.ecr.aws", "ecr-public"),
        ("602401143452.dkr.ecr.us-east-2.amazonaws.com", "ecr"),
        ("123456789012.dkr.ecr.cn-north-1.amazonaws.com.cn", "ecr"),
        ("us-docker.pkg.dev", "gar"),
        ("europe-west1-docker.pkg.dev", "gar"),
        ("gcr.io", "gcr"),
        ("us.gcr.io", "gcr"),
        ("asia.gcr.io", "gcr"),
        ("iad.ocir.io", "ocir"),
        ("myregistry.azurecr.io", "acr"),
        ("unknown.example.com", ""),
        ("quay.io", ""),
    ],
)
def test_classify(host, family):
    assert classify(host) == family
