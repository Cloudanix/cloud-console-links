import logging


logger = logging.getLogger(__name__)


class AzureLinker:
    def get_console_link(self, id: str, primary_ad_domain_name: str = None, iam_entity_type: str = None) -> str:
        if not primary_ad_domain_name and not iam_entity_type:
            logger.error("For IAM entity required `iam_entity_type` and for other entity required\
                 `primary_ad_domain_name`")
            raise ValueError("Invalid parameters provided")
        iam_entities = {
            "user": 'https://portal.azure.com/#blade/Microsoft_AAD_IAM/UserDetailsMenuBlade/Profile/userId/{id}',
            "group": 'https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/{id}',
            "application": 'https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade\
            /Overview/appId/{id}',
        }

        if iam_entity_type and id and iam_entities.get(iam_entity_type, None):
            return eval(f"f'{iam_entities[iam_entity_type]}'").replace(" ", "")

        elif primary_ad_domain_name and id:
            return f"https://portal.azure.com/#@{primary_ad_domain_name}/resource{id}/overview"

        else:
            logger.error('entity id required')
            raise ValueError("Invalid parameters provided")

