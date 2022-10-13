from typing import Dict


def get_links() -> Dict:
    links = {
        "a4b": {  # Alexa for Business
            "address-book": None,
            "conference-provider": None,
            "contact": None,
            "device": None,
            "network-profile": None,
            "profile": None,
            "room": None,
            "schedule": None,
            "skill-group": None,
            "user": None,
        },
        "access-analyzer": {  # IAM Access Analyzer
            "analyzer": 'https://{data.get("region", "")}.{data.get("console", "")}/access-analyzer/home?region=\
                {data.get("region", "")}#/analyzer/{data.get("resource", "")}',
        },
        "acm": {  # AWS Certificate Manager
            "certificate": 'https://{data.get("console", "")}/acm/home?region={data.get("region", "")}#/?id=\
            {data.get("resource", "")}',
        },
        "acm-pca": {  # AWS Certificate Manager Private Certificate Authority
            "certificate-authority": None,
        },
        "amplify": {  # AWS Amplify
            "apps": None,
        },
        "apigateway": {  # Manage Amazon API Gateway
            "api": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/home?region={data.get("region", "")}\
                    #/{data.get("resource", "")}/resources/',
            "stage": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/\
                        home?region={data.get("region", "")}#/{data.get("resource", "")}'
        },
        "appconfig": {  # AWS AppConfig
            "application": None,
            "deploymentstrategy": None,
        },
        "appflow": {  # Amazon AppFlow
            "connectorprofile": None,
            "flow": None,
        },
        "appmesh": {  # AWS App Mesh
            "mesh": None,
        },
        "appmesh-preview": {  # AWS App Mesh Preview
            "mesh": None,
        },
        "appstream": {  # Amazon AppStream 2.0
            "fleet": None,
            "image": None,
            "image-builder": None,
            "stack": None,
        },
        "appsync": {  # AWS AppSync
            "apis": None,
        },
        "artifact": {  # AWS Artifact
            "agreement": None,
            "customer-agreement": None,
            "report-package": None,
        },
        "athena": {  # Amazon Athena
            "datacatalog": None,
            "workgroup": None,
        },
        "autoscaling": {  # Amazon EC2 Auto Scaling
            "autoScalingGroup": None,
            "launchConfiguration": None,
        },
        "aws-marketplace": {  # AWS Marketplace Catalog
        },
        "backup": {  # AWS Backup
            "backup-plan": None,
            "backup-vault": None,
        },
        "batch": {  # AWS Batch
            "job-definition": None,
            "job-queue": None,
        },
        "budgets": {  # AWS Budget Service
            "budget": None,
        },
        "cassandra": {  # Amazon Keyspaces (for Apache Cassandra)
            "": None,
        },
        "catalog": {  # AWS Service Catalog
            "portfolio": None,
            "product": None,
        },
        "chatbot": {  # AWS Chatbot
        },
        "chime": {  # Amazon Chime
            "meeting": None,
        },
        "cloud9": {  # AWS Cloud9
            "environment": None,
        },
        "clouddirectory": {  # Amazon Cloud Directory
            "directory": None,
            "schema": None,
        },
        "cloudformation": {  # AWS CloudFormation
            "changeSet": None,
            "stack": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudformation/home?region={data.get("region", "")}\
            #/stacks/stackinfo?stackId={arn}&# filteringStatus=active&filteringText=&viewNested=true&hideStacks=false',
            "stackset": None,
        },
        "cloudfront": {  # Amazon CloudFront
            "distribution": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudfront/v3/\
                    home?region={data.get("region", "")}#/{data.get("resource", "")}',
            "origin-access-identity": None,
            "streaming-distribution": None,
        },
        "cloudhsm": {  # AWS CloudHSM
            "backup": None,
            "cluster": None,
        },
        "cloudsearch": {  # Amazon CloudSearch
            "domain": None,
        },
        "cloudtrail": {  # AWS CloudTrai
            "trail": 'https://{data.get("console", "")}/cloudtrail/home?region={data.get("region", "")}#/trails/\
            {data.get("resource", "")}',

        },
        "cloudwatch": {  # Amazon CloudWatch
            "alarm": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#alarmsV2:alarm/{data.get("resource", "")}?',
            "metric": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region=data.get("region", "")}#metricsV2:graph=~()',
            "loggroup": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?\
                    region={data.get("region", "")}#logsV2:log-groups/{data.get("resource", "")}',
            "flowlog": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?\
                    region={data.get("region", "")}#logsV2:log-groups/{data.get("resource", "")}',
            "dashboard": None,
            "insight-rule": None,
        },
        "codeartifact": {  # AWS CodeArtifact
            "domain": None,
            "package": None,
            "repository": None,
        },
        "codebuild": {  # AWS CodeBuild
            "build": None,
            "project": None,
            "report": None,
            "report-group": None,
        },
        "codecommit": {  # Amazon CodeGuru Reviewer
        },
        "codedeploy": {  # AWS CodeDeploy
            "application": None,
            "deploymentconfig": None,
            "deploymentgroup": None,
            "instance": None,
        },
        "codeguru-profiler": {  # Amazon CodeGuru Profiler
            "profilingGroup": None,
        },
        "codeguru-reviewer": {  # Amazon CodeGuru Reviewer
            ".+": None,
            "association": None,
        },
        "codepipeline": {  # AWS CodePipeline
            "actiontype": None,
            "webhook": None,
        },
        "codestar": {  # AWS CodeStar
            "project": None,
        },
        "codestar-connections": {  # AWS CodeStar Connections
            "connection": None,
        },
        "codestar-notifications": {  # AWS CodeStar Notifications
            "notificationrule": None,
        },
        "cognito-identity": {  # Amazon Cognito Identity
            "identitypool": None,
        },
        "cognito-idp": {  # Amazon Cognito User Pools
            "userpool": None,
        },
        "cognito-sync": {  # Amazon Cognito Sync
            "identitypool": None,
        },
        "comprehend": {  # Amazon Comprehend
            "document-classifier": None,
            "document-classifier-endpoint": None,
            "entity-recognizer": None,
        },
        "config": {  # AWS Config
            "aggregation-authorization": None,
            "config-aggregator": None,
            "config-rule": None,
            "conformance-pack": None,
            "organization-config-rule": None,
            "organization-conformance-pack": None,
            "remediation-configuration": None,

        },
        "connect": {  # Amazon Connect
            "instance": None,
        },
        "cur": {  # AWS Cost and Usage Report
            "definition": None,
        },
        "dataexchange": {  # AWS Data Exchange
            "data-sets": None,
            "jobs": None,
        },
        "datasync": {  # DataSync
            "agent": None,
            "location": None,
            "task": None,
        },
        "dax": {  # Amazon DynamoDB Accelerator (DAX)
            "cache": None,
        },
        "deepcomposer": {  # AWS DeepComposer
            "audio": None,
            "composition": None,
            "model": None,
        },
        "deeplens": {  # AWS DeepLens
            "device": None,
            "model": None,
            "project": None,
        },
        "deepracer": {  # AWS DeepRacer
            " evaluation_job": None,
            "leaderboard": None,
            "leaderboard_evaluation_job": None,
            "model": None,
            "track": None,
            "training_job": None,
        },
        "detective": {  # Amazon Detective
            "graph": None,
        },
        "devicefarm": {  # AWS Device Farm
            "artifact": None,
            "device": None,
            "deviceinstance": None,
            "devicepool": None,
            "instanceprofile": None,
            "job": None,
            "networkprofile": None,
            "project": None,
            "run": None,
            "sample": None,
            "session": None,
            "suite": None,
            "test": None,
            "testgrid-project": None,
            "testgrid-session": None,
            "upload": None,
            "vpceconfiguration": None,
        },
        "directconnect": {  # AWS Direct Connect
            "dx-gateway": None,
            "dxcon": None,
            "dxlag": None,
            "dxvif": None,
        },
        "dlm": {  # Amazon Data Lifecycle Manager
            "policy": None,
        },
        "dms": {  # AWS Database Migration Service
            "cert": None,
            "endpoint": None,
            "es": None,
            "rep": None,
            "subgrp": None,
            "task": None,
        },
        "ds": {  # AWS Directory Service
            "directory": None,
        },
        "dynamodb": {  # Amazon DynamoDB
            "global-table": None,
            "table": 'https://{data.get("region", "")}.{data.get("console", "")}/dynamodbv2/home?region=\
                {data.get("region", "")}#table?name={data.get("resource", "")}',
        },
        "ec2": {  # AWS Systems Manager
            "capacity-reservation": None,
            "client-vpn-endpoint": None,
            "customer-gateway": None,
            "dedicated-host": None,
            "dhcp-options": None,
            "elastic-gpu": None,
            "fpga-image": None,
            "image": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get("region", "")}#ImageDetails:imageId={data.get("resource", "")}',
            "instance": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get\
                ("region", "")}#InstanceDetails:instanceId={data.get("resource", "")}',
            "internet-gateway": None,
            "key-pair": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get\
                ("region", "")}#KeyPairs:',
            "launch-template": None,
            "local-gateway": None,
            "local-gateway-route-table": None,
            "local-gateway-route-table-virtual-interface-group-association": None,
            "local-gateway-route-table-vpc-association": None,
            "local-gateway-virtual-interface": None,
            "local-gateway-virtual-interface-group": None,
            "network-acl": None,
            "network-interface": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                    home?region={data.get("region", "")}#NetworkInterface:networkInterfaceId={data.get("resource", "")}',
            "placement-group": None,
            "reserved-instances": 'https://{data.get("region", "")}.{data.get("console", "")}/\
                    ec2/home?region={data.get("region", "")}#ReservedInstances:',
            "route-table": None,
            "security-group": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SecurityGroup:groupId={data.get("resource", "")}',
            "snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?\
                    region={data.get("region", "")}#SnapshotDetails:snapshotId={data.get("resource", "")}',
            "spot-instances-request": None,
            "subnet": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SubnetDetails:subnetId={data.get("resource", "")}',
            "traffic-mirror-filter": None,
            "traffic-mirror-filter-rule": None,
            "traffic-mirror-session": None,
            "traffic-mirror-target": None,
            "transit-gateway": None,
            "transit-gateway-attachment": None,
            "transit-gateway-multicast-domain": None,
            "transit-gateway-route-table": None,
            "volume": 'https://u{data.get("region", "")}.{data.get("console", "")}/ec2\
                    /home?region={data.get("region", "")}#VolumeDetails:volumeId=data.get("resource", "")}',
            "vpc": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#VpcDetails:VpcId={data.get("resource", "")}',
            "vpc-endpoint": None,
            "vpc-endpoint-service": None,
            "vpc-flow-log": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region={data.get("region", "")}#subnets:',
            "vpc-peering-connection": None,
            "vpn-connection": None,
            "vpn-gateway": None,
            "elastic-ip": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                    home?region={data.get("region", "")}#ElasticIpDetails:AllocationId={data.get("resource", "")}',
            "beanstalk_environment": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/\
                    home?region={data.get("region", "")}#/environment/dashboard?environmentId={data.get("resource", "")}'

        },
        "ecr": {  # Amazon Elastic Container Registry
            "repository": 'https://{data.get("region", "")}.{data.get("console", "")}/ecr/repositories/{data.get\
                ("resource", "")}?region={data.get("region", "")}',
        },
        "ecs": {  # Amazon Elastic Container Service
            "cluster": None,
            "container-instance": None,
            "service": None,
            "task": None,
            "task-definition": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs\
                    /home?region={data.get("region", "")}#/taskDefinitions/{data.get("resource", "")}',
            "task-set": None,
        },
        "eks": {  # Amazon Elastic Container Service for Kubernetes
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/eks/home?region={data.get\
                ("region", "")}#/clusters/{data.get("resource", "")}',
            "fargateprofile": None,
            "nodegroup": None,
        },
        "elastic-inference": {  # Amazon Elastic Inference
            "elastic-inference-accelerator": None,
        },
        "elasticbeanstalk": {  # AWS Elastic Beanstalk
            "application": None,
            "applicationversion": None,
            "configurationtemplate": None,
            "environment": None,
            "platform": None,
            "solutionstack": None,
        },
        "elasticfilesystem": {  # Amazon Elastic File System
            "access-point": None,
            "file-system": 'https://https://{data.get("region", "")}.{data.get("console", "")}/efs/home?region={data.get("region", "")}#/file-systems/{data.get("resource", "")}',
        },
        "elasticloadbalancing": {  # AWS WAF V2
            "listener": None,
            "listener-rule": None,
            "loadbalancer": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                        home?region={data.get("region", "")}#LoadBalancers:sort=loadBalancerName',
            "targetgroup": None,
        },
        "elasticmapreduce": {  # Amazon Elastic MapReduce
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticmapreduce/home?region={data.get("region", "")}#cluster-details:{data.get("resource", "")}',
            "editor": None,
        },
        "elastictranscoder": {  # Amazon Elastic Transcoder
            "job": None,
            "pipeline": None,
            "preset": None,
        },
        "es": {  # Amazon Elasticsearch Service
            "domain": 'https://{data.get("region", "")}.{data.get("console", "")}/esv3/\
                        home?region={data.get("region", "")}#opensearch/domains/{data.get("resource", "")}',
            "reserved_instance": 'https://{data.get("region", "")}.{data.get("console", "")}/esv3/\
                        home?region={data.get("region", "")}#opensearch/reserved-instances'
        },
        "events": {  # Amazon EventBridge
            "event-bus": 'https://{data.get("region", "")}.{data.get("console", "")}/events/home?region={data.get("region", "")}#/eventbus/{data.get("resource", "")}',
            "event-source": None,
            "rule": None,
        },
        "execute-api": {  # Amazon API Gateway
        },
        "firehose": {  # Amazon Kinesis Firehose
            "deliverystream": 'https://{data.get("region", "")}.{data.get("console", "")}/firehose/home?region={data.get("region", "")}#/details/{data.get("resource", "")}/monitoring',
        },
        "fms": {  # AWS Firewall Manager
            "policy": None,
        },
        "forecast": {  # Amazon Forecast
            "algorithm": None,
            "dataset": None,
            "dataset-group": None,
            "dataset-import-job": None,
            "forecast": None,
            "forecast-export-job": None,
            "predictor": None,
        },
        "freertos": {  # Amazon FreeRTOS
            "configuration": None,
        },
        "fsx": {  # Amazon FSx
            "backup": None,
            "file-system": None,
            "task": None,
        },
        "gamelift": {  # Amazon GameLift
            "alias": None,
            "build": None,
            "fleet": None,
            "gamesessionqueue": None,
            "matchmakingconfiguration": None,
            "matchmakingruleset": None,
            "script": None,
        },
        "glacier": {  # Amazon Glacier
            "vaults": None,
        },
        "globalaccelerator": {  # AWS Global Accelerator
            "accelerator": None,
        },
        "glue": {  # AWS Glue
            "catalog": None,
            "connection": None,
            "crawler": None,
            "database": None,
            "devendpoint": None,
            "job": None,
            "mlTransform": None,
            "table": None,
            "tableVersion": None,
            "trigger": None,
            "userDefinedFunction": None,
            "workflow": None,
        },
        "greengrass": {  # AWS IoT Greengrass
            "": None,
        },
        "groundstation": {  # AWS Ground Station
            "config": None,
            "contact": None,
            "dataflow-endpoint-group": None,
            "groundstation": None,
            "mission-profile": None,
            "satellite": None,
        },
        "guardduty": {  # Amazon GuardDuty
            "detector": None,
        },
        "health": {  # AWS Health APIs and Notifications
            "event": None,
        },
        "honeycode": {  # Amazon Honeycode
            "screen": None,
            "screen-automation": None,
        },
        "iam": {  # AWS Security Token Service
            "access-report": None,
            "assumed-role": None,
            "federated-user": None,
            "group": 'https://{data.get("console", "")}/iamv2/home#/groups/details/{get_resource_path\
            (data.get("resource", ""))}',
            "instance-profile": None,
            "mfa": None,
            "oidc-provider": 'https://{data.get("console", "")}/iam/home?#/providers/{get_arn_string(data)}',
            "policy": 'https://{data.get("console", "")}/iam/home?#/policies/{get_arn_string(data)}',
            "role": 'https://{data.get("console", "")}/iam/home?#/roles/{get_resource_path(data.get("resource", ""))}',
            "saml-provider": None,
            "server-certificate": None,
            "sms-mfa": None,
            "user": 'https://{data.get("console", "")}/iam/home?#/users/{data.get("resource", "")}',
        },
        "imagebuilder": {  # Amazon EC2 Image Builder
            "component": None,
            "distribution-configuration": None,
            "image": None,
            "image-pipeline": None,
            "image-recipe": None,
            "infrastructure-configuration": None,
        },
        "iot": {  # AWS IoT
            "authorizer": None,
            "billinggroup": None,
            "cacert": None,
            "cert": None,
            "client": None,
            "dimension": None,
            "index": None,
            "job": None,
            "mitigationaction": None,
            "otaupdate": None,
            "policy": None,
            "provisioningtemplate": None,
            "rolealias": None,
            "rule": None,
            "scheduledaudit": None,
            "securityprofile": None,
            "stream": None,
            "thing": None,
            "thinggroup": None,
            "thingtype": None,
            "topic": None,
            "topicfilter": None,
            "tunnel": None,
        },
        "iot1click": {  # AWS IoT 1-Click
            "devices": None,
            "projects": None,
        },
        "iotanalytics": {  # AWS IoT Analytics
            "channel": None,
            "dataset": None,
            "datastore": None,
            "pipeline": None,
        },
        "iotevents": {  # AWS IoT Events
            "detectorModel": None,
            "input": None,
        },
        "iotsitewise": {  # AWS IoT SiteWise
            "access-policy": None,
            "asset": None,
            "asset-model": None,
            "dashboard": None,
            "gateway": None,
            "portal": None,
            "project": None,
        },
        "iotthingsgraph": {  # AWS IoT Things Graph
            "Deployment": None,
            "System": None,
            "Workflow": None,
        },
        "kafka": {  # Amazon Managed Streaming for Kafka
            "cluster": None,
        },
        "kendra": {  # Amazon Kendra
            "index": None,
        },
        "kinesis": {  # Amazon Kinesis
            "stream": 'https://{data.get("region", "")}.{data.get("console", "")}/kinesis/home?region={data.get("region", "")}#/streams/details/{data.get("resource", "")}/monitoring',
        },
        "kinesisanalytics": {  # Amazon Kinesis Analytics V2
            "application": None,
        },
        "kinesisvideo": {  # Amazon Kinesis Video Streams
            "channel": None,
            "stream": None,
        },
        "kms": {  # AWS Key Management Service
            "alias": None,
            "key": 'https://{data.get("region", "")}.{data.get("console", "")}/kms/\
                    home?region={data.get("region", "")}#/kms/keys/{data.get("resource", "")}',
        },
        "lambda": {  # AWS Lambda
            "event-source-mapping": None,
            "function": 'https://{data.get("region", "")}.{data.get("console", "")}/lambda/home?region=\
                {data.get("region", "")}#/functions/{data.get("resource", "")}',
        },
        "lex": {  # Amazon Lex
            "bot": None,
            "bot-channel": None,
            "intent": None,
            "slottype": None,
        },
        "license-manager": {  # AWS License Manager
            "license-configuration": None,
        },
        "lightsail": {  # Amazon Lightsail
            "CloudFormationStackRecord": None,
            "Disk": None,
            "DiskSnapshot": None,
            "Domain": None,
            "ExportSnapshotRecord": None,
            "Instance": None,
            "InstanceSnapshot": None,
            "KeyPair": None,
            "LoadBalancer": None,
            "LoadBalancerTlsCertificate": None,
            "PeeredVpc": None,
            "RelationalDatabase": None,
            "RelationalDatabaseSnapshot": None,
            "StaticIp": None,
        },
        "logs": {  # Amazon CloudWatch Logs
            "log-group": 'https://https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#logsV2:log-groups/log-group/{data.get("resource", "")}',
        },
        "machinelearning": {  # Amazon Machine Learning
            "batchprediction": None,
            "datasource": None,
            "evaluation": None,
            "mlmodel": None,
        },
        "macie2": {  # Amazon Macie
            "classification-job": None,
            "custom-data-identifier": None,
            "findings-filter": None,
            "member": None,
        },
        "managedblockchain": {  # Amazon Managed Blockchain
            "invitations": None,
            "members": None,
            "networks": None,
            "nodes": None,
            "proposals": None,
        },
        "mediaconnect": {  # AWS Elemental MediaConnect
            "entitlement": None,
            "flow": None,
            "output": None,
            "source": None,
        },
        "mediaconvert": {  # AWS Elemental MediaConvert
            "certificates": None,
            "jobTemplates": None,
            "jobs": None,
            "presets": None,
            "queues": None,
        },
        "medialive": {  # AWS Elemental MediaLive
            "channel": None,
            "input": None,
            "inputDevice": None,
            "inputSecurityGroup": None,
            "multiplex": None,
            "offering": None,
            "reservation": None,
        },
        "mediapackage": {  # AWS Elemental MediaPackage
            "channels": None,
            "origin_endpoints": None,
        },
        "mediapackage-vod": {  # AWS Elemental MediaPackage VOD
            "assets": None,
            "packaging-configurations": None,
            "packaging-groups": None,
        },
        "mediastore": {  # AWS Elemental MediaStore
            "container": None,
        },
        "mediatailor": {  # AWS Elemental MediaTailor
            "playbackConfiguration": None,
        },
        "mgh": {  # AWS Migration Hub
            "progressUpdateStream": None,
        },
        "mobilehub": {  # AWS Mobile Hub
            "project": None,
        },
        "mobiletargeting": {  # Amazon Pinpoint
            "apps": None,
            "recommenders": None,
            "templates": None,
        },
        "mq": {  # Amazon MQ
            "broker": None,
            "configuration": None,
        },
        "neptune-db": {  # Amazon Neptune
        },
        "networkmanager": {  # Network Manager
            "device": None,
            "global-network": None,
            "link": None,
            "site": None,
        },
        "opsworks": {  # AWS OpsWorks
            "stack": None,
        },
        "organizations": {  # AWS Organizations
            "account": None,
            "handshake": None,
            "organization": 'https://{data.get("region", "")}.{data.get("console", "")}/organizations/v2/home/accounts/{data.get("resource", "")}',
            "ou": None,
            "policy": None,
            "root": None,
        },
        "outposts": {  # AWS Outposts
            "order": None,
            "outpost": None,
            "site": None,
        },
        "personalize": {  # Amazon Personalize
            "algorithm": None,
            "campaign": None,
            "dataset": None,
            "dataset-group": None,
            "dataset-import-job": None,
            "event-tracker": None,
            "feature-transformation": None,
            "recipe": None,
            "schema": None,
            "solution": None,
        },
        "pi": {  # AWS Performance Insights
            "metrics": None,
        },
        "polly": {  # Amazon Polly
            "lexicon": None,
        },
        "qldb": {  # Amazon QLDB
            "ledger": None,
            "stream": None,
        },
        "quicksight": {  # Amazon QuickSight
            "assignment": None,
            "dashboard": None,
            "group": None,
            "template": None,
            "user": None,
        },
        "ram": {  # AWS Resource Access Manager
            "permission": None,
            "resource-share": None,
            "resource-share-invitation": None,
        },
        "rds": {  # Amazon RDS
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/\
                    home?region={data.get("region", "")}#database:id={data.get("resource", "")};is-cluster=true',
            "cluster-endpoint": None,
            "cluster-pg": None,
            "cluster-snapshot": None,
            "db": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region=\
                {data.get("region", "")}#database:id={data.get("resource", "")};is-cluster=false',
            "db-proxy": None,
            "es": None,
            "og": None,
            "pg": None,
            "ri": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#reserved-instances:',
            "secgrp": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SecurityGroup:groupId={data.get("resource", "")}',
            "snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#db-snapshot:engine=sqlserver-ee;id={arn}',
            "subgrp": None,
            "target": None,
            "target-group": None,
        },
        "rds-db": {  # Amazon RDS IAM Authentication
            "dbuser": None,
        },
        "redshift": {  # Amazon Redshift
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region=\
                {data.get("region", "")}#cluster-details?cluster={data.get("resource", "")}',
            "dbgroup": None,
            "dbname": None,
            "dbuser": None,
            "eventsubscription": None,
            "hsmclientcertificate": None,
            "hsmconfiguration": None,
            "parametergroup": None,
            "securitygroup": None,
            "securitygroupingress": None,
            "snapshot": None,
            "snapshotcopygrant": None,
            "snapshotschedule": None,
            "subnetgroup": None,
            "reserved-node": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2\
                        /home?region={data.get("region", "")}#reserved-nodes'
        },
        "rekognition": {  # Amazon Rekognition
            "collection": None,
            "project": None,
            "streamprocessor": None,
        },
        "resource-groups": {  # AWS Resource Groups
            "group": None,
        },
        "robomaker": {  # AWS RoboMaker
            "deployment-fleet": None,
            "deployment-job": None,
            "robot": None,
            "robot-application": None,
            "simulation-application": None,
            "simulation-job": None,
            "simulation-job-batch": None,
        },
        "route53": {  # Amazon Route 53
            "change": None,
            "delegationset": None,
            "healthcheck": 'https://{data.get("console", "")}/route53/healthchecks/home',
            "hostedzone": 'https://{data.get("console", "")}/route53/home?#resource-record-sets:\
            {data.get("resource", "")}',
            "queryloggingconfig": None,
            "trafficpolicy": 'https://{data.get("console", "")}/route53/trafficflow/home#/policy/\
            {data.get("resource", "")}',
            "trafficpolicyinstance": 'https://{data.get("console", "")}/route53/trafficflow/home#/\
            modify-records/edit/{data.get("resource", "")}',
        },
        "route53resolver": {  # Amazon Route 53 Resolver
            "resolver-endpoint": None,
            "resolver-rule": None,
        },
        "s3": {  # Amazon S3
            "": 'https://s3.{data.get("console", "")}/s3/buckets/{data.get("resource", "")}',
                "accesspoint": None,
                "job": None,
        },
        "sagemaker": {  # Amazon SageMaker
            "algorithm": None,
            "app": None,
            "automl-job": None,
            "code-repository": None,
            "compilation-job": None,
            "domain": None,
            "endpoint": None,
            "endpoint-config": None,
            "experiment": None,
            "experiment-trial": None,
            "experiment-trial-component": None,
            "flow-definition": None,
            "human-loop": None,
            "human-task-ui": None,
            "hyper-parameter-tuning-job": None,
            "labeling-job": None,
            "model": None,
            "model-package": None,
            "monitoring-schedule": None,
            "notebook-instance": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/notebook-instances/{data.get("resource", "")}',
            "notebook-instance-lifecycle-config": None,
            "processing-job": None,
            "training-job": None,
            "transform-job": None,
            "user-profile": None,
            "workforce": None,
            "workteam": None,
        },
        "savingsplans": {  # AWS Savings Plans
            "savingsplan": None,
        },
        "schemas": {  # Amazon EventBridge Schemas
            "discoverer": None,
            "registry": None,
            "schema": None,
        },
        "sdb": {  # Amazon SimpleDB
            "domain": None,
        },
        "secretsmanager": {  # AWS Secrets Manager
            "secret": 'https://{data.get("region", "")}.{data.get("console", "")}/secretsmanager/secret?name={data.get("resource", "")}&region ={data.get("region", "")}',
        },
        "securityhub": {  # AWS Security Hub
            "hub": None,
            "product": None,
        },
        "serverlessrepo": {  # AWS Serverless Application Repository
            "applications": None,
        },
        "servicediscovery": {  # AWS Cloud Map
            "namespace": None,
            "service": None,
        },
        "servicequotas": {  # Service Quotas
        },
        "ses": {  # Amazon SES
            "configuration-set": None,
            "custom-verification-email-template": None,
            "dedicated-ip-pool": None,
            "deliverability-test-report": None,
            "identity": 'https://{data.get("region", "")}.{data.get("console", "")}/ses/home?region={data.get("region", "")}#/verified-identities/{data.get("resource", "")}',
            "receipt-filter": None,
            "receipt-rule-set": None,
            "template": None,
        },
        "shield": {  # AWS Shield
            "attack": None,
            "protection": None,
        },
        "signer": {  # AWS Code Signing for Amazon FreeRTOS
            "": None,
        },
        "sns": {  # Amazon SNS
            "": 'https://{data.get("region", "")}.{data.get("console", "")}/sns/v3/home?region={data.get("region", "")}#/topic/{arn}'
        },
        "sqs": {  # Amazon SQS
            "": 'https://{data.get("region", "")}.{data.get("console", "")}/sqs/v2/home?region=\
                {data.get("region", "")}#/queues/https%3A%2F%2Fsqs.{data.get("region", "")}.\
                amazonaws.com%2F{data.get("account", "")}%2F{data.get("resource", "")}',
        },
        "ssm": {  # AWS Systems Manager
            "association": None,
            "automation-definition": None,
            "automation-execution": None,
            "document": None,
            "maintenancewindow": None,
            "managed-instance": None,
            "managed-instance-inventory": None,
            "opsitem": None,
            "parameter": 'https://{data.get("region", "")}.{data.get("console", "")}/systems-manager/parameters/{data.get("resource", "")}/description?region={data.get("region", "")}&tab=Table',
            "patchbaseline": None,
            "resource-data-sync": None,
            "servicesetting": None,
            "session": 'https://{data.get("region", "")}.{data.get("console", "")}/systems-manager/session-manager?region={data.get("region", "")}',
            "windowtarget": None,
            "windowtask": None,
        },
        "states": {  # AWS Step Functions
            "activity": None,
            "execution": None,
            "stateMachine": 'https://{data.get("region", "")}.{data.get("console", "")}/states/home?region=\
                {data.get("region", "")}#/statemachines/view/{get_arn_string(data)}',
        },
        "storagegateway": {  # Amazon Storage Gateway
            "gateway": None,
            "share": None,
            "tape": None,
        },
        "sumerian": {  # Amazon Sumerian
            "project": None,
        },
        "swf": {  # Amazon Simple Workflow Service
            "domain": None,
        },
        "synthetics": {  # Amazon CloudWatch Synthetics
            "canary": None,
        },
        "transfer": {  # AWS Transfer for SFTP
            "server": None,
            "user": None,
        },
        "trustedadvisor": {  # AWS Trusted Advisor
            "checks": None,
        },
        "waf": {  # AWS WAF
            "bytematchset": None,
            "geomatchset": None,
            "ipset": None,
            "ratebasedrule": None,
            "regexmatch": None,
            "regexpatternset": None,
            "rule": None,
            "rulegroup": None,
            "sizeconstraintset": None,
            "sqlinjectionset": None,
            "webacl": None,
            "xssmatchset": None,
        },
        "waf-regional": {  # AWS WAF Regional
            "bytematchset": None,
            "geomatchset": None,
            "ipset": None,
            "ratebasedrule": None,
            "regexmatch": None,
            "regexpatternset": None,
            "rule": None,
            "rulegroup": None,
            "sizeconstraintset": None,
            "sqlinjectionset": None,
            "webacl": None,
            "xssmatchset": None,
        },
        "wafv2": {  # AWS WAF V2
        },
        "wellarchitected": {  # AWS Well-Architected Tool
            "workload": None,
        },
        "worklink": {  # Amazon WorkLink
            "fleet": None,
        },
        "workmail": {  # Amazon WorkMail
            "organization": None,
        },
        "workmailmessageflow": {  # Amazon WorkMail Message Flow
            "message": None,
        },
        "workspaces": {  # Amazon WorkSpaces
            "directory": None,
            "workspace": None,
            "workspacebundle": None,
            "workspaceipgroup": None,
        },
        "xray": {  # AWS X-Ray
            "group": None,
            "sampling-rule": None,
        },
    }

    return links
