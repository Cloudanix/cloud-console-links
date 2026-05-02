import inspect

import pytest

from cloudconsolelink.clouds.aws import (
    AWSLinker,
    get_arn_string,
    get_console,
    get_qualifiers,
    get_resource_path,
)
from cloudconsolelink.clouds.azure import AzureLinker
from cloudconsolelink.clouds.gcp import GCPLinker
from cloudconsolelink.clouds.gcp.links import Resource


GCP_SAMPLE_ARGS = {
    "project_id": "demo-project",
    "zone": "us-central1-a",
    "region": "us-central1",
    "bucket_name": "demo-bucket",
    "instance_name": "demo-instance",
    "network_name": "demo-network",
    "subnet_name": "demo-subnet",
    "disk_name": "demo-disk",
    "rule_name": "demo-rule",
    "managed_service_name": "gateway.example.com",
    "api_name": "demo-api",
    "api_config_name": "demo-config",
    "api_configuration_id": "rollout-1",
    "api_gateway_name": "demo-gateway",
    "bigtable_instance_name": "demo-bigtable",
    "bigtable_cluster_id": "demo-cluster",
    "bigtable_table_id": "demo-table",
    "cloud_function_name": "demo-function",
    "kms_key_ring_name": "demo-ring",
    "kms_key_name": "demo-key",
    "dns_zone_name": "demo-zone",
    "dns_rrset_name": "www.demo.example.",
    "dns_type": "A",
    "gke_cluster_name": "demo-gke",
    "sql_instance_name": "demo-sql",
    "service_account_unique_id": "123456789012345678901",
    "role_id": "organizations/123/roles/demoRole",
    "group_unique_id": "group-123",
    "firestore_collection_name": "demo-collection",
    "cloud_run_service_name": "demo-run-service",
    "topic_id": "demo-topic",
    "dataproc_cluster_name": "demo-dataproc",
    "uptimecheck_config_name": "projects/demo/uptimeCheckConfigs/config-123",
    "alert_policy_name": "projects/demo/alertPolicies/policy-123",
    "instance_group_name": "demo-group",
    "health_check_name": "demo-health-check",
    "backend_service_name": "demo-backend",
    "ssl_policy_name": "demo-ssl-policy",
    "backend_bucket_name": "demo-backend-bucket",
    "dns_policy_name": "demo-dns-policy",
    "policy_name": "demo-policy",
    "database_name": "demo-database",
    "api_key_id": "demo-api-key",
    "subscription_id": "demo-subscription",
}


def _gcp_method_name(resource_name: str) -> str:
    if resource_name == "cloud_monitoring_uptime_check_config":
        return "cloud_monitoring_uptimecheck_config"
    return resource_name


def _gcp_resource_name(method_name: str) -> str:
    if method_name == "cloud_monitoring_uptimecheck_config":
        return "cloud_monitoring_uptime_check_config"
    return method_name


def _resource_method_kwargs(method_name: str) -> dict[str, str]:
    resource = Resource()
    signature = inspect.signature(getattr(resource, method_name))
    kwargs: dict[str, str] = {}
    for name, parameter in signature.parameters.items():
        if parameter.kind is inspect.Parameter.VAR_KEYWORD:
            continue
        kwargs[name] = GCP_SAMPLE_ARGS[name]
    return kwargs


GCP_RESOURCE_METHODS = sorted(
    method_name
    for method_name, member in inspect.getmembers(Resource, predicate=inspect.isfunction)
    if not method_name.startswith("_")
)


@pytest.mark.parametrize("method_name", GCP_RESOURCE_METHODS)
def test_gcp_resource_methods_return_console_urls(method_name: str):
    resource = Resource()

    out_link = getattr(resource, method_name)(**_resource_method_kwargs(method_name))

    assert out_link.replace(" ", "").startswith("https://console.cloud.google.com/")


@pytest.mark.parametrize("method_name", GCP_RESOURCE_METHODS)
def test_gcp_resource_methods_validate_required_parameters(method_name: str):
    resource = Resource()
    kwargs = _resource_method_kwargs(method_name)
    first_arg = next(iter(kwargs))
    kwargs[first_arg] = ""

    with pytest.raises(ValueError, match="Invalid parameters provided"):
        getattr(resource, method_name)(**kwargs)


@pytest.mark.parametrize("method_name", GCP_RESOURCE_METHODS)
def test_gcp_linker_supports_all_resource_builders(method_name: str):
    resource_name = _gcp_resource_name(method_name)
    kwargs = _resource_method_kwargs(method_name)
    expected_link = getattr(Resource(), method_name)(**kwargs).replace(" ", "")

    out_link = GCPLinker().get_console_link(resource_name=resource_name, **kwargs)

    assert out_link == expected_link


def test_gcp_linker_rejects_unknown_resource_name():
    with pytest.raises(ValueError, match="Invalid parameters provided"):
        GCPLinker().get_console_link(resource_name="missing_resource", project_id="demo-project")


def test_azure_supports_all_iam_entity_variants():
    azure = AzureLinker()

    assert (
        azure.get_console_link(id="user-123", iam_entity_type="group")
        == "https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/user-123"
    )
    assert (
        azure.get_console_link(id="app-123", iam_entity_type="application")
        == "https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/Overview/appId/app-123"
    )
    assert (
        azure.get_console_link(
            id="/subscriptions/sub-123/resourceGroups/demo/providers/Microsoft.Authorization/roleAssignments/role-123",
            iam_entity_type="role",
            primary_ad_domain_name="demo.onmicrosoft.com",
        )
        == "https://portal.azure.com/#@demo.onmicrosoft.com/resource/subscriptions/sub-123/resourceGroups/demo/providers/Microsoft.Authorization/roleAssignments/role-123/roles"
    )
    assert (
        azure.get_console_link(
            id="sp-object-123",
            iam_entity_type="service_principal",
            app_id="app-789",
        )
        == "https://portal.azure.com/#view/Microsoft_AAD_IAM/ManagedAppMenuBlade/~/Properties/objectId/sp-object-123/appId/app-789/preferredSingleSignOnMode~/null"
    )
    assert (
        azure.get_console_link(id="contoso.com", iam_entity_type="domain")
        == "https://portal.azure.com/#view/Microsoft_AAD_IAM/DomainPropertiesBladeV2/domainName/contoso.com"
    )


def test_azure_supports_key_vault_secret_and_certificate_links():
    azure = AzureLinker()
    domain = "demo.onmicrosoft.com"

    assert (
        azure.get_console_link(
            id="https://demovault.vault.azure.net/secrets/secret-1",
            primary_ad_domain_name=domain,
        )
        == "https://portal.azure.com/#@demo.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Secret/https://demovault.vault.azure.net/secrets/secret-1"
    )
    assert (
        azure.get_console_link(
            id="https://demovault.vault.azure.net/certificates/cert-1",
            primary_ad_domain_name=domain,
        )
        == "https://portal.azure.com/#@demo.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Certificate/https://demovault.vault.azure.net/certificates/cert-1"
    )


def test_azure_requires_identity_context():
    with pytest.raises(ValueError, match="Invalid parameters provided"):
        AzureLinker().get_console_link(id="/subscriptions/sub-123")


def test_azure_rejects_unknown_iam_entity_without_domain():
    with pytest.raises(ValueError, match="Invalid parameters provided"):
        AzureLinker().get_console_link(id="user-123", iam_entity_type="unknown")


def test_aws_helper_functions_cover_all_arn_shapes():
    assert get_console("aws") == "console.aws.amazon.com"
    assert get_console("aws-us-gov") == "console.amazonaws-us-gov.com"
    assert get_console("aws-cn") == "console.amazonaws.cn"
    assert get_console("aws-iso") == ""

    assert get_arn_string(
        {
            "prefix": "arn",
            "partition": "aws",
            "service": "sns",
            "region": "us-east-1",
            "account": "123456789012",
            "resource": "topic-name",
            "resourceType": "",
        }
    ) == "arn:aws:sns:us-east-1:123456789012:topic-name"
    assert get_arn_string(
        {
            "prefix": "arn",
            "partition": "aws",
            "service": "ec2",
            "region": "us-east-1",
            "account": "123456789012",
            "resourceType": "instance",
            "resource": "i-123",
            "hasPath": True,
        }
    ) == "arn:aws:ec2:us-east-1:123456789012:instance/i-123"
    assert get_arn_string(
        {
            "prefix": "arn",
            "partition": "aws",
            "service": "rds",
            "region": "us-east-1",
            "account": "123456789012",
            "resourceType": "db",
            "resource": "db-123",
            "hasPath": False,
        }
    ) == "arn:aws:rds:us-east-1:123456789012:db:db-123"

    assert get_qualifiers("alpha:beta:gamma") == ["alpha", "beta", "gamma"]
    assert get_resource_path("service/path/resource") == "resource"


def test_aws_linker_validates_bad_arns_and_unknown_services():
    aws = AWSLinker()

    with pytest.raises(ValueError, match="is too short"):
        aws.get_console_link("arn:aws")

    with pytest.raises(ValueError, match="invalid partition"):
        aws.get_console_link("arn:aws-iso:ec2:us-east-1:123456789012:instance/i-123")

    with pytest.raises(ValueError, match="Invalid AWS ARN"):
        aws.get_console_link("not-arn:aws:ec2:us-east-1:123456789012:instance/i-123")

    with pytest.raises(ValueError, match="unknown"):
        aws.get_console_link("arn:aws:not-a-service:us-east-1:123456789012:item/demo")


def test_aws_linker_falls_back_for_service_only_arns():
    aws = AWSLinker()

    assert (
        aws.get_console_link("arn:aws:ec2:us-east-1:123456789012")
        == "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1"
    )


def test_aws_linker_builds_links_for_helper_based_arn_templates():
    aws = AWSLinker()

    assert (
        aws.get_console_link("arn:aws:iam::123456789012:oidc-provider/auth.example.com")
        == "https://console.aws.amazon.com/iam/home?#/providers/arn:aws:iam::123456789012:oidc-provider/auth.example.com"
    )
    assert (
        aws.get_console_link("arn:aws:iam::123456789012:policy/DemoPolicy")
        == "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::123456789012:policy/DemoPolicy"
    )
    assert (
        aws.get_console_link("arn:aws:states:us-east-1:123456789012:stateMachine:demo-machine")
        == "https://us-east-1.console.aws.amazon.com/states/home?region=us-east-1#/statemachines/view/arn:aws:states:us-east-1:123456789012:stateMachine:demo-machine"
    )


def test_aws_linker_builds_links_for_raw_arn_templates():
    aws = AWSLinker()

    assert (
        aws.get_console_link(
            "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/ca-1234"
        )
        == "https://us-east-1.console.aws.amazon.com/acm-pca/home?region=us-east-1#/certificateAuthority?arn=arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/ca-1234"
    )
    assert (
        aws.get_console_link(
            "arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/demo-group/1234567890abcdef"
        )
        == "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#TargetGroups:targetGroupArn=arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/demo-group/1234567890abcdef"
    )
