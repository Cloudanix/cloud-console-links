import logging
import urllib.parse
from typing import Dict

from .errors import ARNTooShortError, InvalidARNError, InvalidPartitionError, InvalidServiceError
from .links import get_links

logger = logging.getLogger(__name__)

SERVICE_HOME_OVERRIDES = {
    "elasticloadbalancing": "https://{region}.{console}/ec2/home?region={region}#LoadBalancers:",
    "logs": "https://{region}.{console}/cloudwatch/home?region={region}#logsV2:log-groups",
    "sns": "https://{region}.{console}/sns/v3/home?region={region}",
    "sqs": "https://{region}.{console}/sqs/v2/home?region={region}",
}


def get_console(partition: str) -> str:
    consoles = {
        "aws": "console.aws.amazon.com",
        "aws-us-gov": "console.amazonaws-us-gov.com",
        "aws-cn": "console.amazonaws.cn",
    }
    return consoles.get(partition, "")


def get_arn_string(data: Dict) -> str:
    if not data.get("resourceType", ""):
        return (
            f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:"
            f"{data.get('region', '')}:{data.get('account', '')}:{data.get('resource', '')}"
        )

    elif data.get("hasPath", ""):
        return (
            f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:"
            f"{data.get('region', '')}:{data.get('account', '')}:{data.get('resourceType', '')}"
            f"/{data.get('resource', '')}"
        )

    else:
        return (
            f"{data.get('prefix', '')}:{data.get('partition', '')}:{data.get('service', '')}:"
            f"{data.get('region', '')}:{data.get('account', '')}:{data.get('resourceType', '')}:"
            f"{data.get('resource', '')}"
        )


def get_qualifiers(resource: str) -> list[str]:
    return resource.split(":")


def get_resource_path(resource: str) -> str:
    return resource.split("/")[-1]


def get_service_home_link(data: Dict) -> str:
    service = str(data.get("service", ""))
    console = str(data.get("console", ""))
    region = str(data.get("region", ""))

    if not service or not console:
        return ""

    if region and service in SERVICE_HOME_OVERRIDES:
        return SERVICE_HOME_OVERRIDES[service].format(
            console=console,
            region=urllib.parse.quote(region),
        )

    host = f"{region}.{console}" if region else console
    path = f"/{service}/home" if region else f"/{service}"
    link = f"https://{host}{path}"
    if region:
        link = f"{link}?region={urllib.parse.quote(region)}"
    return link


class AWSLinker:
    def get_console_link(self, arn: str) -> str:
        logger.debug(f"Start Process for AWS ARN: {arn}")
        arn = arn.strip()
        tokens = arn.split(":")

        if len(tokens) < 5:
            logger.error(f"AWS ARN {arn} is too short")
            raise ARNTooShortError(f"AWS ARN {arn} is too short")

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

        resource_tokens = tokens[5:]

        console = get_console(str(data.get("partition", "")))
        if not console:
            logger.error(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
            raise InvalidPartitionError(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
        data["console"] = console

        links = get_links()

        if data["prefix"] != "arn":
            logger.error(f"Invalid AWS ARN {arn}")
            raise InvalidARNError(f"Invalid AWS ARN {arn}")

        if data["service"] not in links:
            logger.error(f"AWS service {data['service']} unknown")
            raise InvalidServiceError(f"AWS service {data['service']} unknown")

        if not resource_tokens or resource_tokens == [""]:
            return get_service_home_link(data)

        if len(resource_tokens) > 1 and "/" not in resource_tokens[0]:
            data["resourceType"] = resource_tokens[0]
            data["resource"] = ":".join(resource_tokens[1:])
            data["hasPath"] = False

        elif resource_tokens[0].count("/") > 0:
            data["resourceType"] = resource_tokens[0][: resource_tokens[0].index("/")]
            data["resource"] = resource_tokens[0][resource_tokens[0].index("/") + 1 :]
            data["hasPath"] = True

        elif resource_tokens[0]:
            data["resourceType"] = ""
            data["resource"] = resource_tokens[0]
            data["hasPath"] = False

        else:  # pragma: no cover – defensive; unreachable via str.split
            logger.error(f"Invalid AWS ARN {arn}")
            raise InvalidARNError(f"Invalid AWS ARN {arn}")

        if not links.get(data["service"], {}).get(data["resourceType"], None):
            logger.error(
                f"AWS service {data['service']} resource type {data['resourceType']} not supported",
            )
            return get_service_home_link(data)

        template_context = {
            "arn": arn,
            "data": data,
            "get_arn_string": get_arn_string,
            "get_qualifiers": get_qualifiers,
            "get_resource_path": get_resource_path,
        }
        data["resource"] = urllib.parse.quote(str(data["resource"]))
        return eval(
            f"f'{links[data['service']][data['resourceType']]}'",
            {"__builtins__": {}},
            template_context,
        ).replace(
            " ",
            "",
        )


__all__ = [
    "ARNTooShortError",
    "AWSLinker",
    "InvalidARNError",
    "InvalidPartitionError",
    "InvalidServiceError",
    "SERVICE_HOME_OVERRIDES",
    "get_arn_string",
    "get_console",
    "get_qualifiers",
    "get_resource_path",
    "get_service_home_link",
]
