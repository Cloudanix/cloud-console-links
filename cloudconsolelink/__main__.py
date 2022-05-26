import logging

from clouds.aws import get_aws_console_link
from clouds.azure import get_azure_console_link

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_for_aws(arn: str) -> str:
    return get_aws_console_link(arn).replace(" ", "")


def run_for_azure(id: str, active_directory_name: str = None, iam_entity_type: str = None):
    entity_data = {
        "id": id,
        "active_directory_name": active_directory_name,
        "iam_entity_type": iam_entity_type,
    }
    return get_azure_console_link(**entity_data).replace(" ", "")
