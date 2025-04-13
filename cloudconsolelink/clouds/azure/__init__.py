import logging


logger = logging.getLogger(__name__)


class AzureLinker:
    def get_console_link(
        self,
        id: str,
        app_id: str = "",
        primary_ad_domain_name: str = "",
        iam_entity_type: str = "",
    ) -> str:
        if not primary_ad_domain_name and not iam_entity_type:
            logger.error(
                "For IAM entity required `iam_entity_type` and for other entity required `primary_ad_domain_name`",
            )
            raise ValueError("Invalid parameters provided")
        iam_entities = {
            "user": "https://portal.azure.com/#blade/Microsoft_AAD_IAM/UserDetailsMenuBlade/Profile/userId/{id}",
            "group": "https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/{id}",
            "application": "https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade\
            /Overview/appId/{id}",
            "role": "https://portal.azure.com/#@{primary_ad_domain_name}/resource{id}/roles",
            "service_principal": "https://portal.azure.com/#view/Microsoft_AAD_IAM/ManagedAppMenuBlade/~/Properties/\
                                objectId/{id}/appId/{app_id}/preferredSingleSignOnMode~/null",
            "domain": "https://portal.azure.com/#view/Microsoft_AAD_IAM/DomainPropertiesBladeV2/domainName/{id}",
        }

        if iam_entity_type and id and iam_entities.get(iam_entity_type):
            if iam_entity_type == "role" and primary_ad_domain_name:
                return eval(f"f'{iam_entities[iam_entity_type]}'").replace(" ", "")
            elif iam_entity_type == "service_principal" and app_id:
                return eval(f"f'{iam_entities[iam_entity_type]}'").replace(" ", "")
            else:
                return eval(f"f'{iam_entities[iam_entity_type]}'").replace(" ", "")

        elif primary_ad_domain_name and id:
            if id.startswith("https"):
                if "/keys/" in id:
                    return f"https://portal.azure.com/#@{primary_ad_domain_name}/asset/Microsoft_Azure_KeyVault/Key/{id}"
                elif "/secrets/" in id:
                    return f"https://portal.azure.com/#@{primary_ad_domain_name}/asset/Microsoft_Azure_KeyVault/Secret/{id}"
                elif "/certificates/" in id:
                    return f"https://portal.azure.com/#@{primary_ad_domain_name}/asset/Microsoft_Azure_KeyVault/Certificate/{id}"

            return f"https://portal.azure.com/#@{primary_ad_domain_name}/resource{id}/overview"

        else:
            logger.error("entity id required")
            raise ValueError("Invalid parameters provided")
