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
