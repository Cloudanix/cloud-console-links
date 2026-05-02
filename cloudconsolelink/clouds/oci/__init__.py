import logging

from .links import Resource

logger = logging.getLogger(__name__)


class OCILinker:
    def get_console_link(
        self,
        resource_name: str = "",
        **kwargs,
    ) -> str:
        if not resource_name:
            logger.error("resource_name is required")
            raise ValueError("Invalid parameters provided")

        resource = Resource()

        resources = {
            # Compute
            "compute_instance": resource.compute_instance,
            "compute_image": resource.compute_image,
            "instance_pool": resource.instance_pool,
            "boot_volume": resource.boot_volume,
            "block_volume": resource.block_volume,
            "dedicated_vm_host": resource.dedicated_vm_host,
            # Networking
            "vcn": resource.vcn,
            "subnet": resource.subnet,
            "security_list": resource.security_list,
            "network_security_group": resource.network_security_group,
            "route_table": resource.route_table,
            "internet_gateway": resource.internet_gateway,
            "nat_gateway": resource.nat_gateway,
            "service_gateway": resource.service_gateway,
            "drg": resource.drg,
            "load_balancer": resource.load_balancer,
            "network_load_balancer": resource.network_load_balancer,
            "public_ip": resource.public_ip,
            "dhcp_options": resource.dhcp_options,
            "local_peering_gateway": resource.local_peering_gateway,
            "network_firewall": resource.network_firewall,
            "network_firewall_policy": resource.network_firewall_policy,
            # Object Storage
            "bucket": resource.bucket,
            # Database
            "db_system": resource.db_system,
            "autonomous_database": resource.autonomous_database,
            "mysql_db_system": resource.mysql_db_system,
            "nosql_table": resource.nosql_table,
            "postgresql_db_system": resource.postgresql_db_system,
            # IAM
            "compartment": resource.compartment,
            "user": resource.user,
            "group": resource.group,
            "policy": resource.policy,
            "dynamic_group": resource.dynamic_group,
            "identity_domain": resource.identity_domain,
            # Containers / OKE
            "oke_cluster": resource.oke_cluster,
            "container_instance": resource.container_instance,
            "container_repository": resource.container_repository,
            "artifact_repository": resource.artifact_repository,
            # Functions
            "functions_application": resource.functions_application,
            # Security
            "vault": resource.vault,
            "key": resource.key,
            "secret": resource.secret,
            "bastion": resource.bastion,
            "cloud_guard_target": resource.cloud_guard_target,
            "waf_policy": resource.waf_policy,
            "vulnerability_scanning_target": resource.vulnerability_scanning_target,
            # Observability
            "alarm": resource.alarm,
            "notification_topic": resource.notification_topic,
            "log_group": resource.log_group,
            "apm_domain": resource.apm_domain,
            "streaming": resource.streaming,
            "connector": resource.connector,
            "events_rule": resource.events_rule,
            # DevOps
            "devops_project": resource.devops_project,
            "devops_build_pipeline": resource.devops_build_pipeline,
            "devops_deploy_pipeline": resource.devops_deploy_pipeline,
            # Resource Manager
            "stack": resource.stack,
            # Data & AI
            "data_science_project": resource.data_science_project,
            "data_catalog": resource.data_catalog,
            "data_flow_application": resource.data_flow_application,
            "data_integration_workspace": resource.data_integration_workspace,
            # API Gateway
            "api_gateway": resource.api_gateway,
            "api_deployment": resource.api_deployment,
            # DNS
            "dns_zone": resource.dns_zone,
            # Email
            "email_sender": resource.email_sender,
            # File Storage
            "file_system": resource.file_system,
            "mount_target": resource.mount_target,
            # Queue
            "queue": resource.queue,
            # Service home pages
            "compute_home": resource.compute_home,
            "networking_home": resource.networking_home,
            "object_storage_home": resource.object_storage_home,
            "database_home": resource.database_home,
            "identity_home": resource.identity_home,
            "oke_home": resource.oke_home,
        }

        if resource_name not in resources:
            logger.error(f"Invalid resource_name - {resource_name}")
            raise ValueError("Invalid parameters provided")

        return resources[resource_name](**kwargs).replace(" ", "")
