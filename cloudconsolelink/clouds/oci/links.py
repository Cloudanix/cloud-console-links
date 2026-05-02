import logging


logger = logging.getLogger(__name__)

BASE = "https://cloud.oracle.com"


class Resource:
    # --- Compute ---
    def compute_instance(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/compute/instances/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def compute_image(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/compute/images/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def instance_pool(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/compute/instance-pools/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def boot_volume(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/block-storage/boot-volumes/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def block_volume(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/block-storage/volumes/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def dedicated_vm_host(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/compute/dedicated-vm-hosts/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Networking ---
    def vcn(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/vcns/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def subnet(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/subnets/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def security_list(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/security-lists/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def network_security_group(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/network-security-groups/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def route_table(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/route-tables/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def internet_gateway(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/internet-gateways/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def nat_gateway(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/nat-gateways/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def service_gateway(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/service-gateways/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def drg(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/drgs/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def load_balancer(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/load-balancers/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def network_load_balancer(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/network-load-balancers/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def public_ip(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/public-ips/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def dhcp_options(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/dhcp-options/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def local_peering_gateway(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/networking/local-peering-gateways/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def network_firewall(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/network-firewall/firewalls/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def network_firewall_policy(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/network-firewall/firewall-policies/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Object Storage ---
    def bucket(self, region: str, namespace: str, bucket_name: str, **kwargs) -> str:
        if region and namespace and bucket_name:
            return f"{BASE}/object-storage/buckets/{namespace}/{bucket_name}?region={region}"
        logger.error("region, namespace, and bucket_name required")
        raise ValueError("Invalid parameters provided")

    # --- Database ---
    def db_system(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/db-systems/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def autonomous_database(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/autonomous-database/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def mysql_db_system(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/mysql/db-systems/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def nosql_table(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/nosql/tables/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def postgresql_db_system(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/postgresql/db-systems/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Identity & Access Management ---
    def compartment(self, ocid: str, **kwargs) -> str:
        if ocid:
            return f"{BASE}/identity/compartments/{ocid}"
        logger.error("ocid required")
        raise ValueError("Invalid parameters provided")

    def user(self, ocid: str, **kwargs) -> str:
        if ocid:
            return f"{BASE}/identity/users/{ocid}"
        logger.error("ocid required")
        raise ValueError("Invalid parameters provided")

    def group(self, ocid: str, **kwargs) -> str:
        if ocid:
            return f"{BASE}/identity/groups/{ocid}"
        logger.error("ocid required")
        raise ValueError("Invalid parameters provided")

    def policy(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/identity/policies/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def dynamic_group(self, ocid: str, **kwargs) -> str:
        if ocid:
            return f"{BASE}/identity/dynamic-groups/{ocid}"
        logger.error("ocid required")
        raise ValueError("Invalid parameters provided")

    def identity_domain(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/identity/domains/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Container & Kubernetes ---
    def oke_cluster(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/containers/clusters/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def container_instance(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/container-instances/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def container_repository(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/container-registry/repositories/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def artifact_repository(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/artifacts/repositories/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Functions / Serverless ---
    def functions_application(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/functions/applications/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Security ---
    def vault(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/security/vaults/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def key(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/security/keys/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def secret(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/security/vaults/secrets/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def bastion(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/bastion/bastions/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def cloud_guard_target(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/cloud-guard/targets/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def waf_policy(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/waf/policies/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def vulnerability_scanning_target(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/vulnerability-scanning/targets/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Observability & Management ---
    def alarm(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/monitoring/alarms/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def notification_topic(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/notification/topics/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def log_group(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/logging/log-groups/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def apm_domain(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/apm/domains/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def streaming(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/streaming/streams/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def connector(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/connector-hub/connectors/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def events_rule(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/events/rules/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- DevOps ---
    def devops_project(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/devops/projects/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def devops_build_pipeline(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/devops/build-pipelines/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def devops_deploy_pipeline(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/devops/deploy-pipelines/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Resource Manager ---
    def stack(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/resource-manager/stacks/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Data & AI ---
    def data_science_project(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/data-science/projects/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def data_catalog(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/data-catalog/catalogs/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def data_flow_application(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/data-flow/applications/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def data_integration_workspace(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/data-integration/workspaces/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- API Gateway ---
    def api_gateway(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/api-gateway/gateways/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def api_deployment(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/api-gateway/deployments/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- DNS ---
    def dns_zone(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/dns/zones/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Email ---
    def email_sender(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/email-delivery/senders/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- File Storage ---
    def file_system(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/file-storage/file-systems/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    def mount_target(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/file-storage/mount-targets/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Queue ---
    def queue(self, region: str, ocid: str, **kwargs) -> str:
        if region and ocid:
            return f"{BASE}/queue/queues/{ocid}?region={region}"
        logger.error("region and ocid required")
        raise ValueError("Invalid parameters provided")

    # --- Service home pages ---
    def compute_home(self, region: str, **kwargs) -> str:
        if region:
            return f"{BASE}/compute/instances?region={region}"
        logger.error("region required")
        raise ValueError("Invalid parameters provided")

    def networking_home(self, region: str, **kwargs) -> str:
        if region:
            return f"{BASE}/networking/vcns?region={region}"
        logger.error("region required")
        raise ValueError("Invalid parameters provided")

    def object_storage_home(self, region: str, **kwargs) -> str:
        if region:
            return f"{BASE}/object-storage/buckets?region={region}"
        logger.error("region required")
        raise ValueError("Invalid parameters provided")

    def database_home(self, region: str, **kwargs) -> str:
        if region:
            return f"{BASE}/db-systems?region={region}"
        logger.error("region required")
        raise ValueError("Invalid parameters provided")

    def identity_home(self, **kwargs) -> str:
        return f"{BASE}/identity/compartments"

    def oke_home(self, region: str, **kwargs) -> str:
        if region:
            return f"{BASE}/containers/clusters?region={region}"
        logger.error("region required")
        raise ValueError("Invalid parameters provided")
