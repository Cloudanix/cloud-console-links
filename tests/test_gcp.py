import pytest

from cloudconsolelink.clouds.gcp import GCPLinker

gcp = GCPLinker()


def test_storage_bucket():

    bucket_name = "xyz"
    resource_name = "storage_bucket"
    expected_link = "https://console.cloud.google.com/storage/browser/xyz"

    out_link = gcp.get_console_link(bucket_name=bucket_name, resource_name=resource_name)

    assert out_link == expected_link


def test_compute_instance():
    instance_name = "xyz"
    project_id = "12345"
    zone = "us-east-1"
    resource_name = "compute_instance"
    expected_link = "https://console.cloud.google.com/compute/instancesDetail/zones/\
        us-east-1/instances/xyz?project=12345&tab=details"

    out_link = gcp.get_console_link(
        instance_name=instance_name,
        resource_name=resource_name, project_id=project_id, zone=zone,
    )

    assert out_link == expected_link.replace(" ", "")


def test_cloud_armor_policy():
    project_id = "12345"
    policy_name = "policy-1"
    resource_name = "cloud_armor_policy"
    expected_link = "https://console.cloud.google.com/net-security/securitypolicies/details/policy-1?project=12345"

    out_link = gcp.get_console_link(
        project_id=project_id,
        policy_name=policy_name,
        resource_name=resource_name,
    )

    assert out_link == expected_link


def test_cloud_armor_policy_requires_policy_name():
    with pytest.raises(ValueError):
        gcp.get_console_link(
            project_id="12345",
            rule_name="policy-1",
            resource_name="cloud_armor_policy",
        )


def test_cloud_tasks_queue():
    project_id = "12345"
    region = "us-central1"
    instance_name = "queue-1"
    resource_name = "cloud_tasks_queue"
    expected_link = "https://console.cloud.google.com/cloudtasks/queue/us-central1/queue-1?project=12345"

    out_link = gcp.get_console_link(
        project_id=project_id,
        region=region,
        instance_name=instance_name,
        resource_name=resource_name,
    )

    assert out_link == expected_link


def test_cloud_spanner_instance():
    project_id = "12345"
    instance_name = "spanner-1"
    resource_name = "cloud_spanner_instance"
    expected_link = "https://console.cloud.google.com/spanner/instances/spanner-1/details/databases?project=12345"

    out_link = gcp.get_console_link(
        project_id=project_id,
        instance_name=instance_name,
        resource_name=resource_name,
    )

    assert out_link == expected_link


def test_cloud_spanner_database():
    project_id = "12345"
    instance_name = "spanner-1"
    database_name = "db-1"
    resource_name = "cloud_spanner_database"
    expected_link = "https://console.cloud.google.com/spanner/instances/spanner-1/databases/db-1/details?project=12345"

    out_link = gcp.get_console_link(
        project_id=project_id,
        instance_name=instance_name,
        database_name=database_name,
        resource_name=resource_name,
    )

    assert out_link == expected_link


def test_cloud_spanner_database_without_database_name():
    out_link = gcp.get_console_link(
        project_id="12345",
        instance_name="spanner-1",
        resource_name="cloud_spanner_database",
    )
    assert out_link == "https://console.cloud.google.com/spanner/instances/spanner-1/databases?project=12345"


def test_cloud_spanner_database_requires_params():
    with pytest.raises(ValueError):
        gcp.get_console_link(resource_name="cloud_spanner_database", project_id="12345")


P = "demo-project"
BASE = "https://console.cloud.google.com"


@pytest.mark.parametrize(
    "resource_name, kwargs, expected",
    [
        (
            "gke_node_pool",
            {"zone": "us-central1", "gke_cluster_name": "c1", "node_pool_name": "pool-1"},
            f"{BASE}/kubernetes/nodepool/us-central1/c1/pool-1?project={P}",
        ),
        (
            "dataflow_job",
            {"region": "us-central1", "job_id": "2026-01-01_00_00_00-123"},
            f"{BASE}/dataflow/jobs/us-central1/2026-01-01_00_00_00-123?project={P}",
        ),
        (
            "compute_image",
            {"image_name": "img-1"},
            f"{BASE}/compute/imagesDetail/projects/{P}/global/images/img-1?project={P}",
        ),
        (
            "compute_image",
            {"image_name": "debian-12", "image_project": "debian-cloud"},
            f"{BASE}/compute/imagesDetail/projects/debian-cloud/global/images/debian-12?project={P}",
        ),
        ("project", {}, f"{BASE}/home/dashboard?project={P}"),
        ("bigquery_dataset", {"dataset_id": "ds"}, f"{BASE}/bigquery?project={P}&p={P}&d=ds&page=dataset"),
        (
            "bigquery_table",
            {"dataset_id": "ds", "table_id": "t1"},
            f"{BASE}/bigquery?project={P}&p={P}&d=ds&t=t1&page=table",
        ),
        ("sql_database", {"sql_instance_name": "db1"}, f"{BASE}/sql/instances/db1/databases?project={P}"),
        ("spanner_backup", {"instance_name": "sp1"}, f"{BASE}/spanner/instances/sp1/backups?project={P}"),
        (
            "target_ssl_proxy",
            {"instance_name": "px"},
            f"{BASE}/net-services/loadbalancing/advanced/targetSslProxies/details/px?project={P}",
        ),
        (
            "firestore_database",
            {"database_name": "(default)"},
            f"{BASE}/firestore/databases/-default-/data/panel?project={P}",
        ),
        ("firestore_database", {"database_name": "db2"}, f"{BASE}/firestore/databases/db2/data/panel?project={P}"),
        (
            "firestore_index",
            {"database_name": "(default)"},
            f"{BASE}/firestore/databases/-default-/indexes/composite?project={P}",
        ),
        ("firestore_index", {}, f"{BASE}/firestore/indexes/composite?project={P}"),
        ("container_registry", {}, f"{BASE}/artifacts?project={P}"),
        ("cloud_monitoring_metric_descriptor", {}, f"{BASE}/monitoring/metrics-explorer?project={P}"),
        (
            "compute_forwarding_rule",
            {"rule_name": "fr", "region": "us-east1"},
            f"{BASE}/net-services/loadbalancing/advanced/forwardingRules/details/regions/us-east1/"
            f"forwardingRules/fr?project={P}",
        ),
        (
            "compute_forwarding_rule",
            {"rule_name": "fr", "region": "global"},
            f"{BASE}/net-services/loadbalancing/advanced/globalForwardingRules/details/fr?project={P}",
        ),
        (
            "compute_forwarding_rule",
            {"rule_name": "fr"},
            f"{BASE}/net-services/loadbalancing/advanced/globalForwardingRules/details/fr?project={P}",
        ),
        (
            "artifact_registry_repository",
            {"region": "us", "instance_name": "repo"},
            f"{BASE}/artifacts/docker/{P}/us/repo?project={P}",
        ),
        (
            "artifact_registry_repository",
            {"region": "us", "instance_name": "repo", "repository_format": "NPM"},
            f"{BASE}/artifacts/npm/{P}/us/repo?project={P}",
        ),
        (
            "dns_resource_record_set",
            {"dns_zone_name": "z1", "dns_rrset_name": "www.example.com.", "dns_type": "A"},
            f"{BASE}/net-services/dns/zones/z1/rrsets/www.example.com./A/view?project={P}",
        ),
        (
            "dns_resource_record_set",
            {"dns_zone_name": "z1", "dns_rrset_name": "www.example.com."},
            f"{BASE}/net-services/dns/zones/z1/details?project={P}",
        ),
    ],
)
def test_project_scoped_links(resource_name, kwargs, expected):
    assert gcp.get_console_link(resource_name=resource_name, project_id=P, **kwargs) == expected


@pytest.mark.parametrize("org_id", ["organizations/123", "123"])
def test_organization(org_id):
    expected = f"{BASE}/iam-admin/settings?organizationId=123"
    assert gcp.get_console_link(resource_name="organization", organization_id=org_id) == expected


@pytest.mark.parametrize("folder_id", ["folders/456", "456"])
def test_folder(folder_id):
    expected = f"{BASE}/iam-admin/iam?folder=456"
    assert gcp.get_console_link(resource_name="folder", folder_id=folder_id) == expected
