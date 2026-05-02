import logging


logger = logging.getLogger(__name__)


class Resource:
    def storage_bucket(self, bucket_name: str, **keward) -> str:
        if bucket_name:
            return f"https://console.cloud.google.com/storage/browser/{bucket_name}"
        logger.error("bucket_name required")
        raise ValueError("Invalid parameters provided")

    def compute_instance(
        self,
        instance_name: str,
        project_id: str,
        zone: str,
        **keward,
    ):
        if instance_name and zone and project_id:
            return (
                f"https://console.cloud.google.com/compute/instancesDetail/zones/{zone}/\
                instances/{instance_name}?project={project_id}&tab=details"
            )
        logger.error("instance_name and zone and project_id required")
        raise ValueError("Invalid parameters provided")

    def compute_instance_vpc_network(
        self,
        project_id: str,
        network_name: str,
        **keward,
    ):
        if network_name and project_id:
            return f"https://console.cloud.google.com/networking/networks/details/\
                {network_name}?project={project_id}&cloudshell=false&pageTab=SUBNETS"
        logger.error("network_name and project_id required")
        raise ValueError("Invalid parameters provided")

    def compute_instance_vpc_network_subnet(
        self,
        project_id: str,
        region: str,
        subnet_name: str,
        **keward,
    ):
        if region and project_id and subnet_name:
            return f"https://console.cloud.google.com/networking/subnetworks/details/\
                {region}/{subnet_name}?project={project_id}"
        logger.error("region and project_id and subnet_name required")
        raise ValueError("Invalid parameters provided")

    def compute_instance_disk(
        self,
        project_id: str,
        zone: str,
        disk_name: str,
        **keward,
    ):
        if zone and project_id and disk_name:
            return (
                f"https://console.cloud.google.com/compute/disksDetail/zones/{zone}/disks/\
                {disk_name}?project={project_id}"
            )
        logger.error("zone and project_id and disk_name required")
        raise ValueError("Invalid parameters provided")

    def compute_firewall_rule(self, project_id: str, rule_name: str, **keward):
        if project_id and rule_name:
            return f"https://console.cloud.google.com/networking/firewalls/details/\
                {rule_name}?project={project_id}"
        logger.error("project_id and rule_name required")
        raise ValueError("Invalid parameters provided")

    def compute_forwarding_rule(
        self,
        project_id: str,
        rule_name: str,
        region: str,
        **keward,
    ):
        if project_id and rule_name and region:
            return f"https://console.cloud.google.com/net-services/loadbalancing/advanced/\
                forwardingRules/details/regions/{region}/forwardingRules/{rule_name}?project={project_id}"
        logger.error("project_id and rule_name and region required")
        raise ValueError("Invalid parameters provided")

    def api(self, project_id: str, managed_service_name: str, api_name: str, **keward):
        if project_id and managed_service_name and api_name:
            return (
                f"https://console.cloud.google.com/api-gateway/api/{api_name}/servicename/\
                {managed_service_name}/overview?cloudshell=false&project={project_id}"
            )
        logger.error("project_id and managed_service_name and api_name required")
        raise ValueError("Invalid parameters provided")

    def api_config(
        self,
        project_id: str,
        managed_service_name: str,
        api_name: str,
        api_config_name: str,
        api_configuration_id: str,
        **keward,
    ):
        if (
            project_id
            and managed_service_name
            and api_name
            and api_config_name
            and api_configuration_id
        ):
            return f"https://console.cloud.google.com/api-gateway/api/{api_name}/servicename/\
                {managed_service_name}/configs/{api_config_name}/rollout/{api_configuration_id}/\
                    details?project={project_id}"
        logger.error(
            "project_id and managed_service_name and api_name and api_config_name and api_configuration_id required",
        )
        raise ValueError("Invalid parameters provided")

    def api_gateway(
        self,
        project_id: str,
        region: str,
        api_gateway_name: str,
        **keward,
    ):
        if project_id and region and api_gateway_name:
            return f"https://console.cloud.google.com/api-gateway/gateway/{api_gateway_name}/\
                location/{region}?project={project_id}"
        logger.error("project_id and region and api_gateway_name required")
        raise ValueError("Invalid parameters provided")

    def big_table_instance(
        self,
        project_id: str,
        bigtable_instance_name: str,
        **keward,
    ):
        if project_id and bigtable_instance_name:
            return f"https://console.cloud.google.com/bigtable/instances/{bigtable_instance_name}/\
                overview?project={project_id}"
        logger.error("project_id and bigtable_instance_name required")
        raise ValueError("Invalid parameters provided")

    def big_table_cluster(
        self,
        project_id: str,
        bigtable_instance_name: str,
        bigtable_cluster_id: str,
        **keward,
    ):
        if project_id and bigtable_instance_name and bigtable_cluster_id:
            return f"https://console.cloud.google.com/bigtable/instances/{bigtable_instance_name}/\
                clusters/{bigtable_cluster_id}?project={project_id}"
        logger.error(
            "project_id and bigtable_instance_name and bigtable_cluster_id required",
        )
        raise ValueError("Invalid parameters provided")

    def big_table(
        self,
        project_id: str,
        bigtable_instance_name: str,
        bigtable_table_id: str,
        **keward,
    ):
        if project_id and bigtable_instance_name and bigtable_table_id:
            return f"https://console.cloud.google.com/bigtable/instances/{bigtable_instance_name}/tables/\
                {bigtable_table_id}/overview?project={project_id}"
        logger.error(
            "project_id and bigtable_instance_name and bigtable_table_id required",
        )
        raise ValueError("Invalid parameters provided")

    def big_table_backup(
        self,
        project_id: str,
        bigtable_instance_name: str,
        bigtable_table_id: str,
        **keward,
    ):
        if project_id and bigtable_instance_name and bigtable_table_id:
            return f"https://console.cloud.google.com/bigtable/instances/{bigtable_instance_name}/\
                backups;tableId={bigtable_table_id}?project={project_id}"
        logger.error(
            "project_id and bigtable_instance_name and bigtable_table_id required",
        )
        raise ValueError("Invalid parameters provided")

    def cloud_function(
        self,
        project_id: str,
        cloud_function_name: str,
        region: str,
        **keward,
    ):
        if project_id and cloud_function_name and region:
            return f"https://console.cloud.google.com/functions/details/{region}/\
                {cloud_function_name}?project={project_id}"
        logger.error("project_id and cloud_function_name and region required")
        raise ValueError("Invalid parameters provided")

    def kms_key_ring(
        self,
        project_id: str,
        kms_key_ring_name: str,
        region: str,
        **keward,
    ):
        if project_id and kms_key_ring_name and region:
            return (
                f"https://console.cloud.google.com/security/kms/keyring/manage/{region}/\
                {kms_key_ring_name}/key?project={project_id}"
            )
        logger.error("project_id and kms_key_ring_name and region required")
        raise ValueError("Invalid parameters provided")

    def kms_key(
        self,
        project_id: str,
        kms_key_ring_name: str,
        region: str,
        kms_key_name: str,
        **keward,
    ):
        if project_id and kms_key_ring_name and region and kms_key_name:
            return f"https://console.cloud.google.com/security/kms/key/manage/{region}/\
                {kms_key_ring_name}/{kms_key_name}?project={project_id}"
        logger.error(
            "project_id and kms_key_ring_name and region and kms_key_name required",
        )
        raise ValueError("Invalid parameters provided")

    def dns_zone(self, project_id: str, dns_zone_name: str, **keward):
        if project_id and dns_zone_name:
            return f"https://console.cloud.google.com/net-services/dns/zones/{dns_zone_name}/\
                details?project={project_id}"
        logger.error("project_id and dns_zone_name required")
        raise ValueError("Invalid parameters provided")

    def dns_resource_record_set(
        self,
        project_id: str,
        dns_zone_name: str,
        dns_rrset_name: str,
        dns_type: str,
        **keward,
    ):
        if project_id and dns_zone_name and dns_rrset_name and dns_type:
            return f"https://console.cloud.google.com/net-services/dns/zones/{dns_zone_name}/\
                rrsets/{dns_rrset_name}/{dns_type}/view?project={project_id}"
        logger.error(
            "project_id and dns_zone_name and dns_rrset_name and dns_type required",
        )
        raise ValueError("Invalid parameters provided")

    def gke_cluster(self, project_id: str, zone: str, gke_cluster_name: str, **keward):
        if project_id and zone and gke_cluster_name:
            return (
                f"https://console.cloud.google.com/kubernetes/clusters/details/{zone}/\
                {gke_cluster_name}/details?project={project_id}"
            )
        logger.error("project_id and zone and gke_cluster_name required")
        raise ValueError("Invalid parameters provided")

    def sql_instance(self, project_id: str, sql_instance_name: str, **keward):
        if project_id and sql_instance_name:
            return (
                f"https://console.cloud.google.com/sql/instances/{sql_instance_name}/\
                overview?project={project_id}"
            )
        logger.error("project_id and sql_instance_name required")
        raise ValueError("Invalid parameters provided")

    def sql_user(self, project_id: str, sql_instance_name: str, **keward):
        if project_id and sql_instance_name:
            return (
                f"https://console.cloud.google.com/sql/instances/{sql_instance_name}/\
                users?project={project_id}"
            )
        logger.error("project_id and sql_instance_name required")
        raise ValueError("Invalid parameters provided")

    def service_account(
        self,
        project_id: str,
        service_account_unique_id: str,
        **keward,
    ):
        if project_id and service_account_unique_id:
            return (
                f"https://console.cloud.google.com/iam-admin/serviceaccounts/details/\
                {service_account_unique_id}?project={project_id}"
            )
        logger.error("project_id and service_account_unique_id required")
        raise ValueError("Invalid parameters provided")

    def service_account_key(
        self,
        project_id: str,
        service_account_unique_id: str,
        **keward,
    ):
        if project_id and service_account_unique_id:
            return (
                f"https://console.cloud.google.com/iam-admin/serviceaccounts/details/\
                {service_account_unique_id}/keys?project={project_id}"
            )
        logger.error("project_id and service_account_unique_id required")
        raise ValueError("Invalid parameters provided")

    def iam_role(self, project_id: str, role_id: str, **keward):
        if project_id and role_id:
            role_id = role_id.replace("/", "<")
            return f"https://console.cloud.google.com/iam-admin/roles/details/{role_id}?project={project_id}"
        logger.error("project_id and role_id required")
        raise ValueError("Invalid parameters provided")

    def iam_group(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/projectselector2/\
                    iam-admin/groups?orgonly=true&project={project_id}&supportedpurview=organizationId"
        logger.error("group_unique_id and organization_id required")
        raise ValueError("Invalid parameters provided")

    def iam_user(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/iam-admin/iam?orgonly=true&project={project_id}&\
                supportedpurview=organizationId"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def firestore_collection(
        self,
        project_id: str,
        firestore_collection_name: str,
        **keward,
    ):
        if project_id and firestore_collection_name:
            return f"https://console.cloud.google.com/firestore/data/{firestore_collection_name}?project={project_id}"
        logger.error("project_id and firestore_collection_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_run_revision(
        self,
        project_id: str,
        cloud_run_service_name: str,
        region: str,
        **keward,
    ):
        if project_id and cloud_run_service_name and region:
            return f"https://console.cloud.google.com/run/detail/{region}/{cloud_run_service_name}/\
                revisions?project={project_id}"
        logger.error("project_id and cloud_run_service_name and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_run_service(
        self,
        project_id: str,
        cloud_run_service_name: str,
        region: str,
        **keward,
    ):
        if project_id and cloud_run_service_name and region:
            return f"https://console.cloud.google.com/run/detail/{region}/{cloud_run_service_name}/\
                general?project={project_id}"
        logger.error("project_id and cloud_run_service_name and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_pubsub_topic(self, project_id: str, topic_id: str, **keward):
        if project_id and topic_id:
            return (
                f"https://console.cloud.google.com/cloudpubsub/topic/detail/{topic_id}?\
                project={project_id}"
            )
        logger.error("project_id and topic_id is  required")
        raise ValueError("Invalid parameters provided")

    def cloud_logging_metric(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/logs/metrics?project={project_id}"
        logger.error("project_id  is  required ")
        raise ValueError("Invalid parameters provided")

    def dataproc_cluster(
        self,
        project_id: str,
        dataproc_cluster_name: str,
        region: str,
        **keward,
    ):
        if project_id and dataproc_cluster_name and region:
            return f"https://console.cloud.google.com/dataproc/clusters/{dataproc_cluster_name}/\
                monitoring?region={region}&project={project_id}"
        logger.error("project_id and dataproc_cluster_name and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_logging_sink(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/logs/router?project={project_id}"
        logger.error("project_id  required")
        raise ValueError("Invalid parameters provided")

    def cloud_monitoring_notification_channels(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/monitoring/alerting/notifications?project={project_id}"
        logger.error("project_id  required")
        raise ValueError("Invalid parameters provided")

    def cloud_monitoring_uptimecheck_config(
        self,
        project_id: str,
        uptimecheck_config_name: str,
        **keward,
    ):
        if project_id and uptimecheck_config_name:
            config_id = uptimecheck_config_name.split("/")[-1]
            return f"https://console.cloud.google.com/monitoring/uptime/{config_id}?project={project_id}"
        logger.error("project_id and cloud_monitoring_uptimecheck_config_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_monitoring_alert_policy(
        self,
        project_id: str,
        alert_policy_name: str,
        **keward,
    ):
        if project_id and alert_policy_name:
            policy_id = alert_policy_name.split("/")[-1]
            return f"https://console.cloud.google.com/monitoring/alerting/policies/{policy_id}?project={project_id}"
        logger.error("project_id and cloud_monitoring_alert_policy_name required")
        raise ValueError("Invalid parameters provided")

    def global_instance_group(
        self,
        project_id: str,
        instance_group_name: str,
        zone: str,
        **keward,
    ):
        if project_id and instance_group_name and zone:
            return f"https://console.cloud.google.com/compute/instanceGroups/\
                    details/{zone}/{instance_group_name}?project={project_id}"
        logger.error("project_id and zone and instance_group_name required")
        raise ValueError("Invalid parameters provided")

    def regional_instance_group(
        self,
        project_id: str,
        instance_group_name: str,
        region: str,
        **keward,
    ):
        if project_id and instance_group_name and region:
            return f"https://console.cloud.google.com/compute/instanceGroups/\
                    details/{region}/{instance_group_name}?project={project_id}"
        logger.error("project_id and region and instance_group_name required")
        raise ValueError("Invalid parameters provided")

    def regional_health_check(
        self,
        project_id: str,
        health_check_name: str,
        region: str,
        **keward,
    ):
        if project_id and health_check_name and region:
            return f"https://console.cloud.google.com/compute/healthChecks/details/\
                    regions/{region}/{health_check_name}?project={project_id}"
        logger.error("project_id and region and health_check_name required")
        raise ValueError("Invalid parameters provided")

    def global_health_check(self, project_id: str, health_check_name: str, **keward):
        if project_id and health_check_name:
            return f"https://console.cloud.google.com/compute/healthChecks\
                    /details/{health_check_name}?project={project_id}"
        logger.error("project_id and health_check_name required")
        raise ValueError("Invalid parameters provided")

    def regional_backend_service(
        self,
        project_id: str,
        backend_service_name: str,
        region: str,
        **keward,
    ):
        if project_id and backend_service_name and region:
            return (
                f"https://console.cloud.google.com/net-services/loadbalancing/advanced/regionBackendServices\
                    /details/{region}/{backend_service_name}?project={project_id}"
            )
        logger.error("project_id and region and backend_service_name required")
        raise ValueError("Invalid parameters provided")

    def global_backend_service(
        self,
        project_id: str,
        backend_service_name: str,
        **keward,
    ):
        if project_id and backend_service_name:
            return f"https://console.cloud.google.com/net-services/loadbalancing\
                    /advanced/backendServices/details/{backend_service_name}?project={project_id}"
        logger.error("project_id and backend_service_name required")
        raise ValueError("Invalid parameters provided")

    def ssl_policy(self, project_id: str, ssl_policy_name: str, **keward):
        if project_id and ssl_policy_name:
            return f"https://console.cloud.google.com/net-security/\
                    sslpolicies/details/{ssl_policy_name}?project={project_id}"
        logger.error("project_id and ssl_policy_name required")
        raise ValueError("Invalid parameters provided")

    def backend_bucket(self, project_id: str, backend_bucket_name: str, **keward):
        if project_id and backend_bucket_name:
            return (
                f"https://console.cloud.google.com/net-services/loadbalancing/advanced\
                    /backendBuckets/details/{backend_bucket_name}?project={project_id}"
            )
        logger.error("project_id and backend_bucket_name required")
        raise ValueError("Invalid parameters provided")

    def dns_policy(self, project_id: str, dns_policy_name: str, **keward):
        if project_id and dns_policy_name:
            return f"https://console.cloud.google.com/net-services/\
                    dns/policies/{dns_policy_name}/view?project={project_id}"
        logger.error("project_id and dns_policy_name required")
        raise ValueError("Invalid parameters provided")

    def api_key(self, project_id: str, api_key_id: str, **keward):
        if project_id and api_key_id:
            return f"https://console.cloud.google.com/apis/credentials/\
                    key/{api_key_id}?project={project_id}"
        logger.error("project_id and api_key_id required")
        raise ValueError("Invalid parameters provided")

    def firestore_index(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/firestore/indexes/\
                    composite?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def cloud_pubsub_subscription(
        self,
        project_id: str,
        subscription_id: str,
        **keward,
    ):
        if project_id and subscription_id:
            return f"https://console.cloud.google.com/cloudpubsub/subscription/\
                    detail/{subscription_id}?project={project_id}"
        logger.error("project_id and subscription_name required")
        raise ValueError("Invalid parameters provided")

    def cloudrun_domain(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/run/domains?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def iam_domain(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/iam-admin/\
                    iam?orgonly=true&project={project_id}&supportedpurview=organizationId"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def bigquery_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/bigquery?referrer=search&project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def cdn_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/net-services/cdn/list?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def dns_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/net-services/dns/zones?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def load_balancer_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/net-services/loadbalancing/list/loadBalancers?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def vpc_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/networking/networks/list?project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def apigateway_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/api-gateway/api?referrer=search&project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def cloudrun_home(self, project_id: str, **keward):
        if project_id:
            return f"https://console.cloud.google.com/run?referrer=search&project={project_id}"
        logger.error("project_id required")
        raise ValueError("Invalid parameters provided")

    def cloud_armor_policy(self, project_id: str, rule_name: str, **keward):
        if project_id and rule_name:
            return f"https://console.cloud.google.com/net-security/securitypolicies/details/{rule_name}?project={project_id}"
        logger.error("project_id and rule_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_build_trigger(self, project_id: str, region: str, **keward):
        if project_id and region:
            return f"https://console.cloud.google.com/cloud-build/triggers;region={region}?project={project_id}"
        logger.error("project_id and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_composer_environment(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/composer/environments/detail/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_scheduler_job(self, project_id: str, region: str, **keward):
        if project_id and region:
            return f"https://console.cloud.google.com/cloudscheduler?project={project_id}&region={region}"
        logger.error("project_id and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_tasks_queue(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/cloudtasks/queue/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_spanner_instance(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/spanner/instances/{instance_name}/details/databases?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_spanner_database(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/spanner/instances/{instance_name}/databases?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def artifact_registry_repository(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/artifacts/docker/{project_id}/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def secret_manager_secret(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/security/secret-manager/secret/{instance_name}?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def memorystore_redis_instance(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/memorystore/redis/locations/{region}/instances/{instance_name}/details/overview?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def memorystore_memcached_instance(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/memorystore/memcached/locations/{region}/instances/{instance_name}/details/overview?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_nat_gateway(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/net-services/nat/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_router(self, project_id: str, region: str, instance_name: str, **keward):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/hybrid/routers/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def vpn_tunnel(self, project_id: str, region: str, instance_name: str, **keward):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/hybrid/vpn/tunnels/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def vpn_gateway(self, project_id: str, region: str, instance_name: str, **keward):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/hybrid/vpn/gateways/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def vertex_ai_model(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/vertex-ai/models/{instance_name}?project={project_id}&region={region}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def vertex_ai_endpoint(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/vertex-ai/endpoints/{instance_name}?project={project_id}&region={region}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def vertex_ai_dataset(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/vertex-ai/datasets/{instance_name}?project={project_id}&region={region}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def workflows_workflow(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/workflows/workflow/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def eventarc_trigger(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/eventarc/triggers/{instance_name}?project={project_id}&region={region}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def alloydb_cluster(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/alloydb/locations/{region}/clusters/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def alloydb_instance(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/alloydb/locations/{region}/clusters/{instance_name}/instances?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_filestore_instance(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/filestore/instances/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def target_http_proxy(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/net-services/loadbalancing/advanced/targetHttpProxies/details/{instance_name}?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def target_https_proxy(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/net-services/loadbalancing/advanced/targetHttpsProxies/details/{instance_name}?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def url_map(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/net-services/loadbalancing/advanced/urlMaps/details/{instance_name}?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")

    def network_endpoint_group(
        self,
        project_id: str,
        zone: str,
        instance_name: str,
        **keward,
    ):
        if project_id and zone and instance_name:
            return f"https://console.cloud.google.com/compute/networkendpointgroups/details/{zone}/{instance_name}?project={project_id}"
        logger.error("project_id, zone and instance_name required")
        raise ValueError("Invalid parameters provided")

    def target_pool(self, project_id: str, region: str, instance_name: str, **keward):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/net-services/loadbalancing/advanced/targetPools/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def interconnect_attachment(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/hybrid/interconnects/attachments/details/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_deploy_pipeline(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/deploy/delivery-pipelines/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def cloud_ids_endpoint(
        self,
        project_id: str,
        region: str,
        instance_name: str,
        **keward,
    ):
        if project_id and region and instance_name:
            return f"https://console.cloud.google.com/net-security/ids/endpoints/{region}/{instance_name}?project={project_id}"
        logger.error("project_id, region and instance_name required")
        raise ValueError("Invalid parameters provided")

    def dialogflow_agent(self, project_id: str, region: str, **keward):
        if project_id and region:
            return f"https://console.cloud.google.com/dialogflow/cx/projects/{project_id}/locations/{region}/agents?project={project_id}"
        logger.error("project_id and region required")
        raise ValueError("Invalid parameters provided")

    def cloud_endpoints_service(self, project_id: str, instance_name: str, **keward):
        if project_id and instance_name:
            return f"https://console.cloud.google.com/endpoints/api/{instance_name}/overview?project={project_id}"
        logger.error("project_id and instance_name required")
        raise ValueError("Invalid parameters provided")
