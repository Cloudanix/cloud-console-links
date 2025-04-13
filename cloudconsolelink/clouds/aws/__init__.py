import logging
import urllib.parse
from typing import Dict

from .links import get_links

logger = logging.getLogger(__name__)


def get_console(partition: str) -> str:
    consoles = {
        "aws": "console.aws.amazon.com",
        "aws-us-gov": "console.amazonaws-us-gov.com",
        "aws-cn": "console.amazonaws.cn",
    }
    return consoles.get(partition, "")


def get_arn_string(data: Dict) -> str:
    if not data.get("resourceType", ""):
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:\
            {data.get('region', '')}:{data.get('account', '')}:{data.get('resource', '')}"

    elif data.get("hasPath", ""):
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:\
            {data.get('region', '')}:{data.get('account', '')}:{data.get('resource_type', '')}\
                /{data.get('resource', '')}"

    else:
        return f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:\
            {data.get('region', '')}:{data.get('account', '')}:{data.get('resource_type', '')}:\
                {data.get('resource', '')}"


def get_qualifiers(resource: str) -> list[str]:
    return resource.split(":")


def get_resource_path(resource: str) -> str:
    return resource.split("/")[-1]


class AWSLinker:
    def get_console_link(self, arn: str) -> str:
        logger.debug(f"Start Process for AWS ARN: {arn}")
        arn = arn.strip()
        firstTokens = arn.split(":")
        tokens = firstTokens[:7]

        try:
            data: dict[str, str | bool] = {
                "prefix": tokens[0],
                "partition": tokens[1],
                "service": tokens[2],
                "region": tokens[3],
                "account": tokens[4],
                "resourceType": "",
                "resource": "",
                "hasPath": False,
            }

        except IndexError:
            logger.error(f"AWS ARN {arn} is to short")
            raise ValueError(f"AWS ARN {arn} is to short")

        if len(tokens) > 6:
            data["resourceType"] = tokens[5]
            data["resource"] = tokens[6]
            data["hasPath"] = False

        elif len(tokens) > 5 and tokens[5].count("/") > 0:
            data["resourceType"] = tokens[5][: tokens[5].index("/")]
            data["resource"] = tokens[5][tokens[5].index("/") + 1 :]
            data["hasPath"] = True

        elif len(tokens) > 5 and tokens[5].count("/") == 0:
            data["resourceType"] = ""
            data["resource"] = tokens[5]
            data["hasPath"] = False

        else:
            logger.error(f"Invalid AWS ARN {arn}")
            raise ValueError(f"Invalid AWS ARN {arn}")

        console = get_console(str(data.get("partition", "")))
        if not console:
            logger.error(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
            raise ValueError(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
        data["console"] = console

        links = get_links()

        if data["prefix"] != "arn":
            logger.error(f"Invalid AWS ARN {arn}")
            raise ValueError(f"Invalid AWS ARN {arn}")

        elif not links.get(data["service"], None):
            logger.error(f"AWS service {data['service']} unknown")
            raise ValueError(f"AWS service {data['service']} unknown")

        elif not links.get(data["service"], {}).get(data["resourceType"], None):
            logger.error(
                f"AWS service {data['service']} resource type {data['resourceType']} not supported",
            )

            # If resource type does not exist, take the user to service home page
            return f"https://console.aws.amazon.com/{data['service']}"

            # raise ValueError(f"AWS service {data['service']} resource type {data['resourceType']} not supported")

        else:
            data["resource"] = urllib.parse.quote(str(data["resource"]))
            return eval(f"f'{links[data['service']][data['resourceType']]}'").replace(
                " ",
                "",
            )
