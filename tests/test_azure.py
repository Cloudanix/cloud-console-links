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