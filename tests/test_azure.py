import pytest


from cloudconsolelink.clouds.azure import AzureLinker

azure = AzureLinker()


def test_azure_iam():

    id = "1234567890"
    iam_entity_type = "user"
    expected_link = "https://portal.azure.com/#blade/Microsoft_AAD_IAM/UserDetailsMenuBlade/\
    Profile/userId/1234567890"

    out_link = azure.get_console_link(id=id, iam_entity_type=iam_entity_type)

    assert out_link == expected_link.replace(" ", "")


def test_azure_management():

    id = "/subscriptions/5592e8dc/resourceGroups/testgroup"
    primary_ad_domain_name = "QA123.onmicrosoft.com"
    expected_link = "https://portal.azure.com/#@QA123.onmicrosoft.com/resource/subscriptions/\
    5592e8dc/resourceGroups/testgroup/overview"

    out_link = azure.get_console_link(id=id, primary_ad_domain_name=primary_ad_domain_name)

    assert out_link == expected_link.replace(" ", "")

def test_azure_key_vault_key():

    id = 'https://demovault.vault.azure.net/keys/demokey'
    primary_ad_domain_name = "QA123.onmicrosoft.com"
    expected_link ='https://portal.azure.com/#@QA123.onmicrosoft.com/asset/Microsoft_Azure_KeyVault/Key/https://demovault.vault.azure.net/keys/demokey'

    out_link = azure.get_console_link(id=id, primary_ad_domain_name=primary_ad_domain_name)

    assert out_link == expected_link.replace(" ", "")

DOMAIN = "QA123.onmicrosoft.com"
BASE = f"https://portal.azure.com/#@{DOMAIN}/resource"
SUB = "/subscriptions/5592e8dc-1111-2222-3333-444455556666"
RG = f"{SUB}/resourceGroups/rg"


def _link(id):
    return azure.get_console_link(id=id, primary_ad_domain_name=DOMAIN)


def test_azure_key_vault_secret_and_certificate():
    secret = "https://demovault.vault.azure.net/secrets/s1/v1"
    cert = "https://demovault.vault.azure.net/certificates/c1"
    assert _link(secret) == f"https://portal.azure.com/#@{DOMAIN}/asset/Microsoft_Azure_KeyVault/Secret/{secret}"
    assert _link(cert) == f"https://portal.azure.com/#@{DOMAIN}/asset/Microsoft_Azure_KeyVault/Certificate/{cert}"


def test_azure_subscription_bare_guid_and_full_id():
    assert _link("5592e8dc-1111-2222-3333-444455556666") == f"{BASE}{SUB}/overview"
    assert _link(SUB) == f"{BASE}{SUB}/overview"


def test_azure_tenant():
    out_link = azure.get_console_link(id="tenant-id", iam_entity_type="tenant")
    assert out_link == "https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview"


def test_azure_top_level_resource_keeps_overview():
    vm = f"{RG}/providers/Microsoft.Compute/virtualMachines/vm1"
    assert _link(vm) == f"{BASE}{vm}/overview"


def test_azure_role_definition_links_scope_access_control():
    role = f"{SUB}/providers/Microsoft.Authorization/roleDefinitions/abc"
    assert _link(role) == f"{BASE}{SUB}/users"
    tenant_role = "/providers/Microsoft.Authorization/roleDefinitions/abc"
    assert _link(tenant_role) == "https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade"


def test_azure_role_assignment_on_resource_links_resource_access_control():
    vm = f"{RG}/providers/Microsoft.Compute/virtualMachines/vm1"
    assert _link(f"{vm}/providers/Microsoft.Authorization/roleAssignments/x") == f"{BASE}{vm}/users"


MG = "/providers/Microsoft.Management/managementGroups/mg1"
POLICY_ASSIGNMENTS = "https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyMenuBlade/~/Assignments"


def test_azure_role_assignment_type_match_is_case_insensitive():
    assert _link(f"{RG}/providers/microsoft.authorization/ROLEASSIGNMENTS/x") == f"{BASE}{RG}/users"


def test_azure_deny_assignment_links_scope_access_control():
    assert _link(f"{SUB}/providers/Microsoft.Authorization/denyAssignments/d1") == f"{BASE}{SUB}/users"


@pytest.mark.parametrize("scope", [SUB, RG, MG])
def test_azure_policy_assignment_links_policy_assignments(scope):
    assert _link(f"{scope}/providers/Microsoft.Authorization/policyAssignments/a1") == POLICY_ASSIGNMENTS


def test_azure_policy_definitions_link_policy_service():
    builtin = "/providers/Microsoft.Authorization/policyDefinitions/0015ea4d-51ff-4ce3-8d8c-f3f8f0179a56"
    assert _link(builtin) == (
        "https://portal.azure.com/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId/"
        "%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F0015ea4d-51ff-4ce3-8d8c-f3f8f0179a56"
    )
    assert _link(f"{SUB}/providers/Microsoft.Authorization/policySetDefinitions/i1") == (
        "https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyMenuBlade/~/Definitions"
    )


def test_azure_other_authorization_types_link_scope_overview():
    assert _link(f"{RG}/providers/Microsoft.Authorization/locks/NoDelete") == f"{BASE}{RG}/overview"
    assert _link(f"{SUB}/providers/Microsoft.Authorization/policyExemptions/e1") == f"{BASE}{SUB}/overview"


@pytest.mark.parametrize(
    "child, parent, blade",
    [
        ("Microsoft.Network/virtualNetworks/v/subnets/s", "Microsoft.Network/virtualNetworks/v", "subnets"),
        ("Microsoft.Network/routeTables/rt/routes/r", "Microsoft.Network/routeTables/rt", "routes"),
        (
            "Microsoft.Network/networkSecurityGroups/n/securityRules/r",
            "Microsoft.Network/networkSecurityGroups/n",
            "inboundSecurityRules",
        ),
        (
            "Microsoft.ContainerService/managedClusters/aks/agentPools/p",
            "Microsoft.ContainerService/managedClusters/aks",
            "nodePools",
        ),
        (
            "Microsoft.Storage/storageAccounts/sa/blobServices/default",
            "Microsoft.Storage/storageAccounts/sa",
            "containersList",
        ),
        (
            "Microsoft.Storage/storageAccounts/sa/blobServices/default/containers/c",
            "Microsoft.Storage/storageAccounts/sa",
            "containersList",
        ),
        (
            "Microsoft.Storage/storageAccounts/sa/fileServices/default/shares/s",
            "Microsoft.Storage/storageAccounts/sa",
            "fileList",
        ),
        (
            "Microsoft.Storage/storageAccounts/sa/queueServices/default/queues/q",
            "Microsoft.Storage/storageAccounts/sa",
            "queueList",
        ),
        (
            "Microsoft.Storage/storageAccounts/sa/tableServices/default/tables/t",
            "Microsoft.Storage/storageAccounts/sa",
            "tableList",
        ),
        (
            "Microsoft.Compute/virtualMachines/vm/extensions/e",
            "Microsoft.Compute/virtualMachines/vm",
            "extensions",
        ),
        (
            "Microsoft.Compute/virtualMachineScaleSets/ss/extensions/e",
            "Microsoft.Compute/virtualMachineScaleSets/ss",
            "extensions",
        ),
        (
            "Microsoft.DocumentDB/databaseAccounts/a/sqlDatabases/d/containers/c",
            "Microsoft.DocumentDB/databaseAccounts/a",
            "dataExplorer",
        ),
        (
            "Microsoft.DocumentDB/databaseAccounts/a/mongodbDatabases/d",
            "Microsoft.DocumentDB/databaseAccounts/a",
            "dataExplorer",
        ),
        ("Microsoft.Web/sites/app/config/web", "Microsoft.Web/sites/app", "configuration"),
        (
            "Microsoft.ContainerRegistry/registries/r/replications/eastus",
            "Microsoft.ContainerRegistry/registries/r",
            "replications",
        ),
        (
            "Microsoft.ContainerRegistry/registries/r/webhooks/w",
            "Microsoft.ContainerRegistry/registries/r",
            "webhooks",
        ),
        # No dedicated blade: parent overview.
        ("Microsoft.ContainerRegistry/registries/r/tasks/t", "Microsoft.ContainerRegistry/registries/r", "overview"),
        ("Microsoft.Web/sites/app/backups/b", "Microsoft.Web/sites/app", "overview"),
        ("Microsoft.Sql/servers/s/administrators/ActiveDirectory", "Microsoft.Sql/servers/s", "overview"),
        # First-class children keep their own page, and their sub-objects link to them.
        ("Microsoft.Sql/servers/s/databases/d", "Microsoft.Sql/servers/s/databases/d", "overview"),
        ("Microsoft.Sql/servers/s/elasticPools/p", "Microsoft.Sql/servers/s/elasticPools/p", "overview"),
        (
            "Microsoft.Sql/servers/s/databases/d/transparentDataEncryption/current",
            "Microsoft.Sql/servers/s/databases/d",
            "overview",
        ),
        ("Microsoft.Web/sites/app/slots/stg", "Microsoft.Web/sites/app/slots/stg", "overview"),
        ("Microsoft.Web/sites/app/slots/stg/config/web", "Microsoft.Web/sites/app/slots/stg", "configuration"),
    ],
)
def test_azure_child_resources_link_parent_blade(child, parent, blade):
    assert _link(f"{RG}/providers/{child}") == f"{BASE}{RG}/providers/{parent}/{blade}"


def test_azure_resources_without_a_page():
    assert _link(f"{SUB}/providers/microsoft.insights/logprofiles/default") == (
        "https://portal.azure.com/#view/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/~/activityLog"
    )
    assert _link(f"{SUB}/providers/Microsoft.Security/securityContacts/default") == f"{BASE}{SUB}/overview"
    assert _link(f"{SUB}/providers/Microsoft.Network/locations/eastus/usages/VirtualNetworks") == (
        f"{BASE}{SUB}/overview"
    )
