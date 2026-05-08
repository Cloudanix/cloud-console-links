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
            logger.debug(
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
            return (
                iam_entities[iam_entity_type]
                .format(id=id, primary_ad_domain_name=primary_ad_domain_name, app_id=app_id)
                .replace(" ", "")
            )

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
            logger.debug("entity id required")
            raise ValueError("Invalid parameters provided")
