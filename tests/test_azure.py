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
    active_directory_name = "QA123"
    expected_link = "https://portal.azure.com/#@QA123.onmicrosoft.com/resource/subscriptions/\
    5592e8dc/resourceGroups/testgroup/overview"

    out_link = azure.get_console_link(id=id, active_directory_name=active_directory_name)

    assert out_link == expected_link.replace(" ", "")
