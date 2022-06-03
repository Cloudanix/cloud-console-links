import logging
from typing import Dict

from .links import Resource

logger = logging.getLogger(__name__)


def build_kwargs(
    resource_name=None,
    project_id=None,
    region=None,
    zone=None,
    bucket_name=None,
    instance_name=None,
    network_name=None,
    subnet_name=None,
    rule_name=None,
    api_name=None,
    managed_service_name=None,
    api_config_name=None,
    api_configuration_id=None,
    api_gateway_name=None,
    bigtable_instance_name=None,
    bigtable_cluster_id=None,
    bigtable_table_id=None,
    cloud_function_name=None,
    kms_key_ring_name=None,
    kms_key_name=None,
    dns_zone_name=None,
    dns_rrset_name=None,
    dns_type=None,
    gke_cluster_name=None,
    sql_instance_name=None,
    service_account_unique_id=None,
    role_id=None,
    group_unique_id=None,
    firestore_collection_name=None,
    cloud_run_service_name=None,
) -> Dict:
    return {
        "resource_name": resource_name,
        "project_id": project_id,
        "region": region,
        "zone": zone,
        "bucket_name": bucket_name,
        "instance_name": instance_name,
        "network_name": network_name,
        "subnet_name": subnet_name,
        "rule_name": rule_name,
        "api_name": api_name,
        "managed_service_name": managed_service_name,
        "api_config_name": api_config_name,
        "api_configuration_id": api_configuration_id,
        "api_gateway_name": api_gateway_name,
        "bigtable_instance_name": bigtable_instance_name,
        "bigtable_cluster_id": bigtable_cluster_id,
        "bigtable_table_id": bigtable_table_id,
        "cloud_function_name": cloud_function_name,
        "kms_key_ring_name": kms_key_ring_name,
        "kms_key_name": kms_key_name,
        "dns_zone_name": dns_zone_name,
        "dns_rrset_name": dns_rrset_name,
        "dns_type": dns_type,
        "gke_cluster_name": gke_cluster_name,
        "sql_instance_name": sql_instance_name,
        "service_account_unique_id": service_account_unique_id,
        "role_id": role_id,
        "group_unique_id": group_unique_id,
        "firestore_collection_name": firestore_collection_name,
        "cloud_run_service_name": cloud_run_service_name,
    }


class GCP:
    def get_console_link(
        self,
        resource_name=None,
        project_id=None,
        region=None,
        zone=None,
        bucket_name=None,
        instance_name=None,
        network_name=None,
        subnet_name=None,
        rule_name=None,
        api_name=None,
        managed_service_name=None,
        api_config_name=None,
        api_configuration_id=None,
        api_gateway_name=None,
        bigtable_instance_name=None,
        bigtable_cluster_id=None,
        bigtable_table_id=None,
        cloud_function_name=None,
        kms_key_ring_name=None,
        kms_key_name=None,
        dns_zone_name=None,
        dns_rrset_name=None,
        dns_type=None,
        gke_cluster_name=None,
        sql_instance_name=None,
        service_account_unique_id=None,
        role_id=None,
        group_unique_id=None,
        firestore_collection_name=None,
        cloud_run_service_name=None,
    ) -> str:
        resource = Resource()

        resources = {
            "storage_bucket": resource.storage_bucket,
            "compute_instance": resource.compute_instance,
        }

        param = build_kwargs(
            resource_name=resource_name,
            project_id=project_id,
            region=region,
            zone=zone,
            bucket_name=bucket_name,
            instance_name=instance_name,
            network_name=network_name,
            subnet_name=subnet_name,
            rule_name=rule_name,
            api_name=api_name,
            managed_service_name=managed_service_name,
            api_config_name=api_config_name,
            api_configuration_id=api_configuration_id,
            api_gateway_name=api_gateway_name,
            bigtable_instance_name=bigtable_instance_name,
            bigtable_cluster_id=bigtable_cluster_id,
            bigtable_table_id=bigtable_table_id,
            cloud_function_name=cloud_function_name,
            kms_key_ring_name=kms_key_ring_name,
            kms_key_name=kms_key_name,
            dns_zone_name=dns_zone_name,
            dns_rrset_name=dns_rrset_name,
            dns_type=dns_type,
            gke_cluster_name=gke_cluster_name,
            sql_instance_name=sql_instance_name,
            service_account_unique_id=service_account_unique_id,
            role_id=role_id,
            group_unique_id=group_unique_id,
            firestore_collection_name=firestore_collection_name,
            cloud_run_service_name=cloud_run_service_name,
        )

        resources_list = list(resources.keys())
        if resource_name in resources_list:
            return resources[resource_name](**param).replace(" ", "")

        logger.error('resource_name invalid')
        raise ValueError("Invalid parameters provided")
