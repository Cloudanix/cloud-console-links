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
    disk_name=None,
    topic_id=None,
    sql_instance_name=None,
    service_account_unique_id=None,
    role_id=None,
    group_unique_id=None,
    firestore_collection_name=None,
    cloud_run_service_name=None,
    dataproc_cluster_name=None,
    uptimecheck_config_name=None,
    alert_policy_name=None,
    instance_group_name=None,
    health_check_name=None,
    backend_service_name=None,
    ssl_policy_name=None,
    backend_bucket_name=None,
    dns_policy_name=None,
    api_key_id=None,
    subscription_id=None,

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
        "disk_name": disk_name,
        "topic_id": topic_id,
        "sql_instance_name": sql_instance_name,
        "service_account_unique_id": service_account_unique_id,
        "role_id": role_id,
        "group_unique_id": group_unique_id,
        "firestore_collection_name": firestore_collection_name,
        "cloud_run_service_name": cloud_run_service_name,
        "dataproc_cluster_name": dataproc_cluster_name,
        "uptimecheck_config_name": uptimecheck_config_name,
        "alert_policy_name": alert_policy_name,
        "instance_group_name": instance_group_name,
        "health_check_name": health_check_name,
        "backend_service_name": backend_service_name,
        "ssl_policy_name": ssl_policy_name,
        "backend_bucket_name": backend_bucket_name,
        "dns_policy_name": dns_policy_name,
        "api_key_id": api_key_id,
        "subscription_id": subscription_id,
    }


class GCPLinker:
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
        disk_name=None,
        topic_id=None,
        sql_instance_name=None,
        service_account_unique_id=None,
        role_id=None,
        group_unique_id=None,
        firestore_collection_name=None,
        cloud_run_service_name=None,
        dataproc_cluster_name=None,
        uptimecheck_config_name=None,
        alert_policy_name=None,
        instance_group_name=None,
        health_check_name=None,
        backend_service_name=None,
        ssl_policy_name=None,
        backend_bucket_name=None,
        dns_policy_name=None,
        api_key_id=None,
        subscription_id=None,
    ) -> str:
        resource = Resource()

        resources = {
            "storage_bucket": resource.storage_bucket,
            "compute_instance": resource.compute_instance,
            "compute_instance_vpc_network": resource.compute_instance_vpc_network,
            "compute_instance_vpc_network_subnet": resource.compute_instance_vpc_network_subnet,
            "compute_instance_disk": resource.compute_instance_disk,
            "compute_firewall_rule": resource.compute_firewall_rule,
            "compute_forwarding_rule": resource.compute_forwarding_rule,
            "api": resource.api,
            "api_config": resource.api_config,
            "api_gateway": resource.api_gateway,
            "big_table_instance": resource.big_table_instance,
            "big_table_cluster": resource.big_table_cluster,
            "big_table": resource.big_table,
            "big_table_backup": resource.big_table_backup,
            "cloud_function": resource.cloud_function,
            "kms_key_ring": resource.kms_key_ring,
            "kms_key": resource.kms_key,
            "dns_zone": resource.dns_zone,
            "dns_resource_record_set": resource.dns_resource_record_set,
            "gke_cluster": resource.gke_cluster,
            "sql_instance": resource.sql_instance,
            "sql_user": resource.sql_user,
            "service_account": resource.service_account,
            "service_account_key": resource.service_account_key,
            "iam_role": resource.iam_role,
            "iam_group": resource.iam_group,
            "iam_user": resource.iam_user,
            "firestore_collection": resource.firestore_collection,
            "cloud_run_revision": resource.cloud_run_revision,
            "cloud_run_service": resource.cloud_run_service,
            "cloud_pubsub_topic": resource.cloud_pubsub_topic,
            "cloud_logging_metric": resource.cloud_logging_metric,
            "dataproc_cluster": resource.dataproc_cluster,
            "cloud_logging_sink": resource.cloud_logging_sink,
            "cloud_monitoring_notification_channels": resource.cloud_monitoring_notification_channels,
            "cloud_monitoring_uptime_check_config": resource.cloud_monitoring_uptimecheck_config,
            "cloud_monitoring_alert_policy": resource.cloud_monitoring_alert_policy,
            "global_instance_group": resource.global_instance_group,
            "regional_instance_group": resource.regional_instance_group,
            "regional_health_check": resource.regional_health_check,
            "global_health_check": resource.global_health_check,
            "regional_backend_service": resource.regional_backend_service,
            "global_backend_service": resource.global_backend_service,
            "ssl_policy": resource.ssl_policy,
            "backend_bucket": resource.backend_bucket,
            "dns_policy": resource.dns_policy,
            "api_key": resource.api_key,
            "firestore_index": resource.firestore_index,
            "cloud_pubsub_subscription": resource.cloud_pubsub_subscription,
            "cloudrun_domain": resource.cloudrun_domain,
            "iam_domain": resource.iam_domain,
            "bigquery": resource.bigquery,
            "cdn": resource.cdn,
            "dns": resource.dns,
            "load_balancer": resource.load_balancer,
            "vpc": resource.vpc,
            "apigateway": resource.apigateway,
            "cloudrun": resource.cloudrun,
        }

        param = build_kwargs(
            resource_name=resource_name,
            project_id=project_id,
            region=region,
            zone=zone,
            bucket_name=bucket_name,
            instance_name=instance_name,
            network_name=network_name,
            disk_name=disk_name,
            topic_id=topic_id,
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
            dataproc_cluster_name=dataproc_cluster_name,
            uptimecheck_config_name=uptimecheck_config_name,
            alert_policy_name=alert_policy_name,
            instance_group_name=instance_group_name,
            health_check_name=health_check_name,
            backend_service_name=backend_service_name,
            ssl_policy_name=ssl_policy_name,
            backend_bucket_name=backend_bucket_name,
            dns_policy_name=dns_policy_name,
            api_key_id=api_key_id,
            subscription_id=subscription_id,
        )

        resources_list = list(resources.keys())
        if resource_name in resources_list:
            return resources[resource_name](**param).replace(" ", "")

        logger.error('resource_name invalid')
        raise ValueError("Invalid parameters provided")
