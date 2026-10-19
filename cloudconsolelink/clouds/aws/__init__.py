import logging
import re
import urllib.parse
from typing import Dict
from typing import Optional

from .errors import ARNTooShortError
from .errors import InvalidARNError
from .errors import InvalidPartitionError
from .errors import InvalidServiceError
from .links import get_links
from .links import HOME_URLS

logger = logging.getLogger(__name__)

_EXPR_RE = re.compile(r"\{([^}]+)\}")


def _render(template: str, data: Dict, arn: str = "") -> str:
    """Render a link template without eval.

    Templates in links.py use patterns like {data.get("region", "")} and {arn}.
    We substitute each {expr} by looking it up in a pre-built context dict after
    stripping all internal whitespace (backslash-continuation lines in the source
    produce spaces inside expressions). Unknown expressions render as empty string.
    """
    resource = str(data.get("resource", ""))
    region = str(data.get("region", ""))
    ctx: Dict[str, str] = {
        **_resource_part_ctx(resource),
        'data.get("region","")': str(data.get("region", "")),
        'data.get("console","")': str(data.get("console", "")),
        'data.get("resource","")': resource,
        'data.get("account","")': str(data.get("account", "")),
        'data.get("service","")': str(data.get("service", "")),
        "get_arn_string(data)": get_arn_string(data),
        'get_resource_path(data.get("resource",""))': get_resource_path(resource),
        "arn": arn,
        "partition": str(data.get("partition", "")),
        "region": region,
        "console": str(data.get("console", "")),
        "resource": resource,
        "account": str(data.get("account", "")),
        "service": str(data.get("service", "")),
    }

    def _sub(m: re.Match) -> str:
        expr = re.sub(
            r"\s+",
            "",
            m.group(1),
        )  # collapse whitespace from line continuations
        if expr not in ctx:
            logger.debug("Unknown template expression %r", expr)
        return ctx.get(expr, "")

    link = _EXPR_RE.sub(_sub, template).replace(" ", "")
    return link if region else _drop_empty_region(link)


def _resource_part_ctx(resource: str) -> Dict[str, str]:
    """Template keys for the pieces of a path-style resource.

    resource_part(N) is the Nth "/"-separated segment (ecs "service/cluster/svc" -> cluster, svc),
    resource_tail is everything after the first "/" (autoscaling "uuid:autoScalingGroupName/name" -> name),
    log_group_id is the log group name in the double-encoded form the CloudWatch console expects.
    """
    raw = urllib.parse.unquote(resource)
    parts = raw.split("/")
    ctx = {
        f"resource_part({i})": urllib.parse.quote(part, safe="")
        for i, part in enumerate(parts)
    }
    ctx["resource_tail"] = urllib.parse.quote(raw.split("/", 1)[-1], safe="")
    log_group = raw[: -len(":*")] if raw.endswith(":*") else raw
    ctx["log_group_id"] = urllib.parse.quote(
        urllib.parse.quote(log_group, safe=""),
        safe="",
    ).replace("%", "$")
    return ctx


def _drop_empty_region(link: str) -> str:
    """Remove the empty region a region-less ARN (IAM, Route 53, SSO, ...) leaves in a template.

    "https://.console..." becomes "https://console..." and a bare "region=" query parameter is dropped.
    """
    link = link.replace("https://.", "https://", 1)
    link = link.replace("?region=&", "?")
    link = re.sub(r"[?&]region=(?=#|$)", "", link)
    return re.sub(r"&region=(?=&)", "", link)


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

    home_template = HOME_URLS.get(service)
    if region and home_template:
        return _render(home_template, data)

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
            logger.debug(f"AWS ARN {arn} is too short")
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
        # API Gateway ARNs are paths: arn:aws:apigateway:us-east-1::/restapis/abc123. Drop the
        # leading "/" so the first segment is the resource type, as in every other path-style ARN.
        if resource_tokens and resource_tokens[0].startswith("/"):
            resource_tokens[0] = resource_tokens[0][1:]

        console = get_console(str(data.get("partition", "")))
        if not console:
            logger.debug(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
            raise InvalidPartitionError(
                f"AWS ARN {arn} has invalid partition (Valid Partitions: aws, aws-us-gov, aws-cn)",
            )
        data["console"] = console

        links = get_links()

        if data["prefix"] != "arn":
            logger.debug(f"Invalid AWS ARN {arn}")
            raise InvalidARNError(f"Invalid AWS ARN {arn}")

        if data["service"] not in links:
            logger.debug(f"AWS service {data['service']} unknown")
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
            logger.debug(f"Invalid AWS ARN {arn}")
            raise InvalidARNError(f"Invalid AWS ARN {arn}")

        # An SNS subscription ARN is the topic ARN plus a subscription id: sns:...:topic:uuid.
        if data["service"] == "sns" and len(resource_tokens) == 2:
            data["resourceType"] = "subscription"

        template = _find_template(
            links[data["service"]],
            str(data["resourceType"]),
            str(data["resource"]),
        )
        if not template:
            logger.debug(
                f"AWS service {data['service']} resource type {data['resourceType']} not supported",
            )
            return get_service_home_link(data)

        data["resource"] = urllib.parse.quote(str(data["resource"]))
        return _render(template, data, arn)


def _find_template(
    service_links: Dict,
    resource_type: str,
    resource: str,
) -> Optional[str]:
    """Pick the template for a resource, preferring a "type/sub-type" key over the plain type.

    Some ARNs carry their real kind one level down: apigateway "restapis/{id}/stages/{stage}" (sub-type in
    the second segment) or wafv2 "regional/webacl/{name}/{id}" (sub-type in the first segment).
    """
    parts = resource.split("/")
    for sub_type in parts[1:2] + parts[:1] if len(parts) > 1 else []:
        template = service_links.get(f"{resource_type}/{sub_type}")
        if template:
            return template
    return service_links.get(resource_type)


__all__ = [
    "ARNTooShortError",
    "AWSLinker",
    "HOME_URLS",
    "InvalidARNError",
    "InvalidPartitionError",
    "InvalidServiceError",
    "get_arn_string",
    "get_console",
    "get_qualifiers",
    "get_resource_path",
    "get_service_home_link",
]
