from typing import Dict
import logging

from .links import get_links

logger = logging.getLogger(__name__)


def get_console(data: Dict):
    if data.get('partition', None) == "aws":
        data['console'] = 'console.aws.amazon.com'
        return data

    elif data.get('partition', None) == "aws-us-gov":
        data['console'] = 'console.amazonaws-us-gov.com'
        return data

    elif data.get('partition', None) == "aws-cn":
        data['console'] = 'console.amazonaws.cn'
        return data

    else:
        return False


def get_string(data: Dict):
    if not data.get('resourceType', None):
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:{data.get('region', '')}:{data.get('account', '')}:{data.get('resource', '')}"

    elif data.get('hasPath', None):
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:{data.get('region', '')}:{data.get('account', '')}:{data.get('resource_type', '')}/{data.get('resource', '')}"

    else:
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:{data.get('region', '')}:{data.get('account', '')}:{data.get('resource_type', '')}:{data.get('resource', '')}"


def get_qualifiers(resource: str):
    return resource.split(":")


def get_pathLast(resource: str):
    return resource.split("/")[-1]


def process_arn(arn: str):
    logger.info(f"Start Process for AWS ARN `{arn}`")
    arn = arn.strip()
    firstTokens = arn.split(":")
    tokens = firstTokens[:7]

    try:
        data = {
            "prefix": tokens[0],
            "partition": tokens[1],
            "service": tokens[2],
            "region": tokens[3],
            "account": tokens[4],
        }

    except IndexError:
        logger.warning(f"AWS ARN `{arn}` is to short")
        return {}

    if len(tokens) > 6:
        data["resourceType"] = tokens[5]
        data["resource"] = tokens[6]
        data["hasPath"] = False

    elif len(tokens) > 5 and tokens[5].count("/") > 0:
        data["resourceType"] = tokens[5][:tokens[5].index("/")]
        data["resource"] = tokens[5][tokens[5].index("/") + 1:]
        data["hasPath"] = True

    elif len(tokens) > 5 and tokens[5].count("/") == 0:
        data["resourceType"] = None
        data["resource"] = tokens[5]
        data["hasPath"] = False

    else:
        logger.warning(f"Invalid AWS ARN `{arn}`")
        return

    data = get_console(data)
    if not data:
        logger.warning(f"AWS ARN `{arn}` has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)")
        return

    links = get_links()

    if data['prefix'] != "arn":
        logger.warning(f"Invalid AWS ARN `{arn}`")
        return

    elif not links.get(data["service"], None):
        logger.warning(f"AWS service `{data['service']}` unknown")
        return

    elif not links.get(data["service"], {}).get(data["resourceType"], None):
        logger.warning(f"AWS service `{data['service']}` resource type `{data['resourceType']}` not supported")
        return

    else:
        return eval(f"f'{links[data['service']][data['resourceType']]}'")
