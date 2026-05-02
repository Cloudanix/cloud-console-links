import pytest

from cloudconsolelink.clouds.oci import OCILinker

oci = OCILinker()

REGION = "us-ashburn-1"
OCID = "ocid1.instance.oc1.iad.abc123"


# --- Compute ---
def test_compute_instance():
    link = oci.get_console_link(
        resource_name="compute_instance", region=REGION, ocid=OCID,
    )
    assert link == f"https://cloud.oracle.com/compute/instances/{OCID}?region={REGION}"


def test_compute_image():
    ocid = "ocid1.image.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="compute_image", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/compute/images/{ocid}?region={REGION}"


def test_boot_volume():
    ocid = "ocid1.bootvolume.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="boot_volume", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/block-storage/boot-volumes/{ocid}?region={REGION}"


def test_block_volume():
    ocid = "ocid1.volume.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="block_volume", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/block-storage/volumes/{ocid}?region={REGION}"


# --- Networking ---
def test_vcn():
    ocid = "ocid1.vcn.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="vcn", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/vcns/{ocid}?region={REGION}"


def test_subnet():
    ocid = "ocid1.subnet.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="subnet", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/subnets/{ocid}?region={REGION}"


def test_security_list():
    ocid = "ocid1.securitylist.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="security_list", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/security-lists/{ocid}?region={REGION}"


def test_network_security_group():
    ocid = "ocid1.networksecuritygroup.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="network_security_group", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/network-security-groups/{ocid}?region={REGION}"


def test_load_balancer():
    ocid = "ocid1.loadbalancer.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="load_balancer", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/load-balancers/{ocid}?region={REGION}"


def test_drg():
    ocid = "ocid1.drg.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="drg", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/networking/drgs/{ocid}?region={REGION}"


# --- Object Storage ---
def test_bucket():
    link = oci.get_console_link(
        resource_name="bucket", region=REGION, namespace="mytenancy", bucket_name="my-bucket",
    )
    assert link == f"https://cloud.oracle.com/object-storage/buckets/mytenancy/my-bucket?region={REGION}"


# --- Database ---
def test_autonomous_database():
    ocid = "ocid1.autonomousdatabase.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="autonomous_database", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/autonomous-database/{ocid}?region={REGION}"


def test_db_system():
    ocid = "ocid1.dbsystem.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="db_system", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/db-systems/{ocid}?region={REGION}"


def test_mysql_db_system():
    ocid = "ocid1.mysqldbsystem.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="mysql_db_system", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/mysql/db-systems/{ocid}?region={REGION}"


# --- IAM ---
def test_compartment():
    ocid = "ocid1.compartment.oc1..abc123"
    link = oci.get_console_link(resource_name="compartment", ocid=ocid)
    assert link == f"https://cloud.oracle.com/identity/compartments/{ocid}"


def test_user():
    ocid = "ocid1.user.oc1..abc123"
    link = oci.get_console_link(resource_name="user", ocid=ocid)
    assert link == f"https://cloud.oracle.com/identity/users/{ocid}"


def test_group():
    ocid = "ocid1.group.oc1..abc123"
    link = oci.get_console_link(resource_name="group", ocid=ocid)
    assert link == f"https://cloud.oracle.com/identity/groups/{ocid}"


def test_policy():
    ocid = "ocid1.policy.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="policy", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/identity/policies/{ocid}?region={REGION}"


# --- Containers ---
def test_oke_cluster():
    ocid = "ocid1.cluster.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="oke_cluster", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/containers/clusters/{ocid}?region={REGION}"


# --- Security ---
def test_vault():
    ocid = "ocid1.vault.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="vault", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/security/vaults/{ocid}?region={REGION}"


def test_secret():
    ocid = "ocid1.vaultsecret.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="secret", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/security/vaults/secrets/{ocid}?region={REGION}"


def test_bastion():
    ocid = "ocid1.bastion.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="bastion", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/bastion/bastions/{ocid}?region={REGION}"


# --- Observability ---
def test_alarm():
    ocid = "ocid1.alarm.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="alarm", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/monitoring/alarms/{ocid}?region={REGION}"


def test_notification_topic():
    ocid = "ocid1.onstopic.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="notification_topic", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/notification/topics/{ocid}?region={REGION}"


# --- DevOps ---
def test_devops_project():
    ocid = "ocid1.devopsproject.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="devops_project", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/devops/projects/{ocid}?region={REGION}"


# --- API Gateway ---
def test_api_gateway():
    ocid = "ocid1.apigateway.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="api_gateway", region=REGION, ocid=ocid)
    assert link == f"https://cloud.oracle.com/api-gateway/gateways/{ocid}?region={REGION}"


# --- Service home pages ---
def test_compute_home():
    link = oci.get_console_link(resource_name="compute_home", region=REGION)
    assert link == f"https://cloud.oracle.com/compute/instances?region={REGION}"


def test_networking_home():
    link = oci.get_console_link(resource_name="networking_home", region=REGION)
    assert link == f"https://cloud.oracle.com/networking/vcns?region={REGION}"


def test_identity_home():
    link = oci.get_console_link(resource_name="identity_home")
    assert link == "https://cloud.oracle.com/identity/compartments"


# --- Error cases ---
def test_invalid_resource_name():
    with pytest.raises(ValueError):
        oci.get_console_link(resource_name="nonexistent_resource", region=REGION, ocid=OCID)


def test_missing_resource_name():
    with pytest.raises(ValueError):
        oci.get_console_link(region=REGION, ocid=OCID)


def test_missing_required_params():
    with pytest.raises(ValueError):
        oci.get_console_link(resource_name="compute_instance", region="", ocid="")


def test_bucket_missing_namespace():
    with pytest.raises(ValueError):
        oci.get_console_link(resource_name="bucket", region=REGION, namespace="", bucket_name="my-bucket")
