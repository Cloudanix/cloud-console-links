import logging
import re
from typing import Tuple
from urllib.parse import quote


logger = logging.getLogger(__name__)

PORTAL = "https://portal.azure.com"
SUBSCRIPTIONS_BLADE = f"{PORTAL}/#view/Microsoft_Azure_Billing/SubscriptionsBlade"
ACTIVITY_LOG_BLADE = f"{PORTAL}/#view/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/~/activityLog"
POLICY_MENU_BLADE = f"{PORTAL}/#view/Microsoft_Azure_Policy/PolicyMenuBlade/~"
POLICY_DETAIL_BLADE = (
    f"{PORTAL}/#blade/Microsoft_Azure_Policy/PolicyDetailBlade/definitionId"
)

_GUID_RE = re.compile(r"^[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$")
_PROVIDERS_RE = re.compile(r"/providers/", re.IGNORECASE)
_AUTHORIZATION_RE = re.compile(
    r"/providers/microsoft\.authorization/([^/]+)",
    re.IGNORECASE,
)

# Microsoft.Authorization types shown on their scope's Access control (IAM) blade.
IAM_BLADE_TYPES = {"roledefinitions", "roleassignments", "denyassignments"}

# Azure Policy objects open in the Policy service, not on their scope. Only the definition blade
# has a documented per-item deep link (Microsoft Learn built-in policy pages). Assignments and
# initiatives stop at their list blade; switch to a per-item blade once one is documented.
POLICY_LINKS = {
    "policyassignments": f"{POLICY_MENU_BLADE}/Assignments",
    "policydefinitions": f"{POLICY_DETAIL_BLADE}/{{id}}",
    "policysetdefinitions": f"{POLICY_MENU_BLADE}/Definitions",
}

# Nested ARM types the portal opens as resources in their own right, so a link keeps
# drilling into them instead of stopping at their parent. Keys are lowercase type paths.
FIRST_CLASS_CHILDREN = {
    "microsoft.sql/servers/databases",
    "microsoft.sql/servers/elasticpools",
    "microsoft.sql/managedinstances/databases",
    "microsoft.web/sites/slots",
}

# Nested ARM types with no page of their own: link to the parent blade that lists them.
# Anything nested and not listed here links to the parent's overview.
CHILD_BLADES = {
    "microsoft.network/virtualnetworks/subnets": "subnets",
    "microsoft.network/routetables/routes": "routes",
    "microsoft.network/networksecuritygroups/securityrules": "inboundSecurityRules",
    "microsoft.network/networksecuritygroups/defaultsecurityrules": "inboundSecurityRules",
    "microsoft.containerservice/managedclusters/agentpools": "nodePools",
    "microsoft.storage/storageaccounts/blobservices": "containersList",
    "microsoft.storage/storageaccounts/fileservices": "fileList",
    "microsoft.storage/storageaccounts/queueservices": "queueList",
    "microsoft.storage/storageaccounts/tableservices": "tableList",
    "microsoft.compute/virtualmachines/extensions": "extensions",
    "microsoft.compute/virtualmachinescalesets/extensions": "extensions",
    "microsoft.documentdb/databaseaccounts/sqldatabases": "dataExplorer",
    "microsoft.documentdb/databaseaccounts/mongodbdatabases": "dataExplorer",
    "microsoft.documentdb/databaseaccounts/cassandrakeyspaces": "dataExplorer",
    "microsoft.documentdb/databaseaccounts/gremlindatabases": "dataExplorer",
    "microsoft.documentdb/databaseaccounts/tables": "dataExplorer",
    "microsoft.web/sites/config": "configuration",
    "microsoft.web/sites/slots/config": "configuration",
    "microsoft.containerregistry/registries/replications": "replications",
    "microsoft.containerregistry/registries/webhooks": "webhooks",
}

# Provider types with no portal page at all: link to the scope they live under.
SCOPE_ONLY_TYPES = {
    "microsoft.security/securitycontacts",
    "microsoft.network/locations",
}


def _anchor_and_blade(segments: list) -> Tuple[str, str]:
    """Split `ns/type/name[/childType/childName...]` into the linkable resource and its blade."""
    type_path = "/".join(segments[:2]).lower()
    end = 3
    while (
        len(segments) > end
        and f"{type_path}/{segments[end].lower()}" in FIRST_CLASS_CHILDREN
    ):
        type_path = f"{type_path}/{segments[end].lower()}"
        end += 2
    if len(segments) <= end:
        return "/".join(segments), "overview"
    return "/".join(segments[:end]), CHILD_BLADES.get(
        f"{type_path}/{segments[end].lower()}",
        "overview",
    )


def _authorization_link(arm_id: str, base: str, authorization: re.Match) -> str:
    """Link a Microsoft.Authorization id. Other types (locks, exemptions, ...) open their scope's overview."""
    resource_type = authorization.group(1).lower()
    if resource_type in POLICY_LINKS:
        return POLICY_LINKS[resource_type].format(id=quote(arm_id, safe=""))
    scope = arm_id[: authorization.start()]
    if not scope:
        return SUBSCRIPTIONS_BLADE
    blade = "users" if resource_type in IAM_BLADE_TYPES else "overview"
    return f"{base}{scope}/{blade}"


def _management_link(arm_id: str, domain: str) -> str:
    base = f"{PORTAL}/#@{domain}/resource"
    if _GUID_RE.match(arm_id):  # bare subscription id
        return f"{base}/subscriptions/{arm_id}/overview"

    authorization = _AUTHORIZATION_RE.search(arm_id)
    if authorization:
        return _authorization_link(arm_id, base, authorization)

    parts = _PROVIDERS_RE.split(arm_id, maxsplit=1)
    if len(parts) == 1:  # subscription or resource group
        return f"{base}{arm_id}/overview"

    scope, tail = parts
    segments = tail.split("/")
    type_path = "/".join(segments[:2]).lower()
    if type_path == "microsoft.insights/logprofiles":
        return ACTIVITY_LOG_BLADE
    if type_path in SCOPE_ONLY_TYPES:
        return f"{base}{scope}/overview" if scope else SUBSCRIPTIONS_BLADE

    anchor, blade = _anchor_and_blade(segments)
    return f"{base}{scope}/providers/{anchor}/{blade}"


def _key_vault_link(uri: str, domain: str) -> str:
    for marker, kind in (
        ("/keys/", "Key"),
        ("/secrets/", "Secret"),
        ("/certificates/", "Certificate"),
    ):
        if marker in uri:
            return f"{PORTAL}/#@{domain}/asset/Microsoft_Azure_KeyVault/{kind}/{uri}"
    return ""


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
            "tenant": "https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview",
        }

        if iam_entity_type and id and iam_entities.get(iam_entity_type):
            return (
                iam_entities[iam_entity_type]
                .format(
                    id=id,
                    primary_ad_domain_name=primary_ad_domain_name,
                    app_id=app_id,
                )
                .replace(" ", "")
            )

        elif primary_ad_domain_name and id:
            if id.startswith("https"):
                key_vault_link = _key_vault_link(id, primary_ad_domain_name)
                if key_vault_link:
                    return key_vault_link

            return _management_link(id, primary_ad_domain_name)

        else:
            logger.debug("entity id required")
            raise ValueError("Invalid parameters provided")
