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


# --- Child resources linked through their parent ---
def test_oke_node_pool():
    ocid = "ocid1.nodepool.oc1.iad.abc123"
    cluster = "ocid1.cluster.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="oke_node_pool", region=REGION, ocid=ocid, cluster_id=cluster)
    assert link == f"https://cloud.oracle.com/containers/clusters/{cluster}/node-pools/{ocid}?region={REGION}"


def test_oke_node_pool_without_cluster_falls_back_to_clusters_list():
    link = oci.get_console_link(resource_name="oke_node_pool", region=REGION, ocid="ocid1.nodepool.oc1.iad.abc123")
    assert link == f"https://cloud.oracle.com/containers/clusters?region={REGION}"


def test_tenancy():
    assert oci.get_console_link(resource_name="tenancy") == "https://cloud.oracle.com/tenancy"


def test_cloud_guard():
    link = oci.get_console_link(resource_name="cloud_guard", region=REGION)
    assert link == f"https://cloud.oracle.com/cloud-guard/overview?region={REGION}"


def test_volume_backup_block_and_boot():
    ocid = "ocid1.volumebackup.oc1.iad.abc123"
    block = oci.get_console_link(resource_name="volume_backup", region=REGION, ocid=ocid, source_kind="BLOCK")
    boot = oci.get_console_link(resource_name="volume_backup", region=REGION, ocid=ocid, source_kind="BOOT")
    default = oci.get_console_link(resource_name="volume_backup", region=REGION, ocid=ocid)
    assert block == f"https://cloud.oracle.com/block-storage/backups/{ocid}?region={REGION}"
    assert boot == f"https://cloud.oracle.com/block-storage/boot-volume-backups/{ocid}?region={REGION}"
    assert default == block


def test_log():
    ocid = "ocid1.log.oc1.iad.abc123"
    group = "ocid1.loggroup.oc1.iad.abc123"
    link = oci.get_console_link(resource_name="log", region=REGION, ocid=ocid, log_group_id=group)
    assert link == f"https://cloud.oracle.com/logging/log-groups/{group}/logs/{ocid}?region={REGION}"


def test_log_without_group_falls_back_to_observability_home():
    link = oci.get_console_link(resource_name="log", region=REGION, ocid="ocid1.log.oc1.iad.abc123")
    assert link == f"https://cloud.oracle.com/monitoring/alarms?region={REGION}"


def test_db_home_and_db_node_link_parent_db_system():
    db_system = "ocid1.dbsystem.oc1.iad.abc123"
    expected = f"https://cloud.oracle.com/db-systems/{db_system}?region={REGION}"
    for name in ("db_home", "db_node"):
        link = oci.get_console_link(resource_name=name, region=REGION, ocid="ocid1.x.oc1.iad.1", db_system_id=db_system)
        assert link == expected
        assert oci.get_console_link(resource_name=name, region=REGION, ocid="ocid1.x.oc1.iad.1") == (
            f"https://cloud.oracle.com/db-systems?region={REGION}"
        )


def test_container_image_links_parent_repository():
    repo = "ocid1.containerrepo.oc1.iad.abc123"
    link = oci.get_console_link(
        resource_name="container_image", region=REGION, ocid="ocid1.containerimage.oc1.iad.1", repository_id=repo,
    )
    assert link == f"https://cloud.oracle.com/container-registry/repositories/{repo}?region={REGION}"


def test_vnic_links_owning_instance():
    instance = "ocid1.instance.oc1.iad.abc123"
    vnic = "ocid1.vnic.oc1.iad.abc123"
    assert oci.get_console_link(resource_name="vnic", region=REGION, ocid=vnic, instance_id=instance) == (
        f"https://cloud.oracle.com/compute/instances/{instance}?region={REGION}"
    )
    assert oci.get_console_link(resource_name="vnic", region=REGION, ocid=vnic) == (
        f"https://cloud.oracle.com/networking/vcns?region={REGION}"
    )
