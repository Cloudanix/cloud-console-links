# What is cloudconsolelink?
This project for generate console links for AWS, GCP and Azure cloud resources

# Install
Run ```pip install cloudconsolelink``` to install our code

# Usage

### Import Package

#### For AWS
```from cloudconsolelink.clouds.aws import AWSLinker```

#### For Azure
```from cloudconsolelink.clouds.azure import AzureLinker```

#### For GCP
```from cloudconsolelink.clouds.gcp import GCPLinker```

#### To get console link
call method ```get_console_link()```


### The Followings Are The Some Example
#### AWS:
```python
from cloudconsolelink.clouds.aws import AWSLinker

aws = AWSLinker()

arn = "arn:aws:ec2:us-east1:1234567890:instance/instance1"

console_link = aws.get_console_link(arn=arn)
```

#### Azure Management:
  ```python
from cloudconsolelink.clouds.azure import AzureLinker

azure = AzureLinker()

id = "/subscriptions/5592e8dc/resourceGroups/testgroup"
primary_ad_domain_name = "QA123.onmicrosoft.com"

console_link = azure.get_console_link(id=id, primary_ad_domain_name=primary_ad_domain_name)
  ```


#### Azure IAM:
```python
from cloudconsolelink.clouds.azure import AzureLinker

azure = AzureLinker()

id = "1234567890"
iam_entity_type = "user"

console_link = azure.get_console_link(id=id, iam_entity_type=iam_entity_type)
```

#### GCP:
  ```python
from cloudconsolelink.clouds.gcp import GCPLinker

gcp = GCPLinker()


bucket_name = "xyz"
resource_name = "storage_bucket"

console_link = gcp.get_console_link(bucket_name=bucket_name, resource_name=resource_name)
  ```

## get_console_link() parameters discription:

### AWS:
  1) arn: arn of resource

### Azure:
#### IAM:
  1) iam_entity_type: type of iam resource(user, group, application)
  2) id: object id

#### Management:
  1) id: id of entity
  2) primary_ad_domain_name: name of the active derectory primary domain

### GCP:
  1) resource_name: name of resource(storage_bucket, compute_instance, compute_instance_vpc_network, compute_instance_vpc_network_subnet, compute_instance_disk, compute_firewall_rule, compute_forwarding_rule, api, api_config, api_gateway, big_table_instance, big_table_cluster, big_table, big_table_backup, cloud_function, kms_key_ring, kms_key, dns_zone, dns_resource_record_set, gke_cluster, sql_instance, sql_user, service_account, service_account_key, iam_role, iam_group, iam_user, firestore_collection, cloud_run_revision, cloud_run_service)
  2) project_id
  3) region
  4) zone
  5) bucket_name
  6) instance_name
  7) network_name
  8) subnet_name
  9) rule_name
  10) api_name
  11) managed_service_name
  12) api_config_name
  13) api_configuration_id
  14) api_gateway_name
  15) bigtable_instance_name
  16) bigtable_cluster_id
  17) bigtable_table_id
  18) cloud_function_name
  19) kms_key_ring_name
  20) kms_key_name
  22) dns_zone_name
  23) dns_rrset_name
  24) dns_type
  25) gke_cluster_name
  26) sql_instance_name
  27) service_account_unique_id
  28) role_id
  29) group_unique_id
  31) firestore_collection_name
  32) cloud_run_service_name


# Who uses cloudconsolelink?
1. [Cloudanix](https://www.cloudanix.com/)
1. {Your company here} :-)

If your organization uses Cloudconsolelink, please file a PR and update this list.
