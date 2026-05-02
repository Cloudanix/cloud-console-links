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
    rule_name = "policy-1"
    resource_name = "cloud_armor_policy"
    expected_link = "https://console.cloud.google.com/net-security/securitypolicies/details/policy-1?project=12345"

    out_link = gcp.get_console_link(
        project_id=project_id,
        rule_name=rule_name,
        resource_name=resource_name,
    )

    assert out_link == expected_link


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
