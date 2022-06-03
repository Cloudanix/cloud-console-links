import logging


logger = logging.getLogger(__name__)


class Azure:
    def get_console_link(self, id: str, active_directory_name: str = None, iam_entity_type: str = None) -> str:
        if not active_directory_name and not iam_entity_type:
            logger.error("For IAM entity required `iam_entity_type` and for other entity required\
                 `active_directory_name`")
            raise ValueError("Invalid parameters provided")
        iam_entities = {
            "user": 'https://portal.azure.com/#blade/Microsoft_AAD_IAM/UserDetailsMenuBlade/Profile/userId/{id}',
            "group": 'https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Overview/groupId/{id}',
            "application": 'https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade\
            /Overview/appId/{id}',
        }

        if iam_entity_type and id and iam_entities.get(iam_entity_type, None):
            return eval(f"f'{iam_entities[iam_entity_type]}'")

        elif active_directory_name and id:
            return f"https://portal.azure.com/#@{active_directory_name}.onmicrosoft.com/resource{id}/overview"

        else:
            logger.error('entity id required')
            raise ValueError("Invalid parameters provided")
