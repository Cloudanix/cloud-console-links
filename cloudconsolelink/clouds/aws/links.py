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
            "certificate-authority": 'https://{data.get("region", "")}.{data.get("console", "")}/acm-pca/home?region={data.get("region", "")}#/certificateAuthority?arn={arn}',
        },
        "amplify": {  # AWS Amplify
            "apps": 'https://{data.get("region", "")}.{data.get("console", "")}/amplify/home?region={data.get("region", "")}#/{data.get("resource", "")}',
        },
        "apigateway": {  # Manage Amazon API Gateway
            "restapis": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/home?region={data.get("region", "")}\
                #/{data.get("resource", "")}/resources/',
            "stages": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/\
                        home?region={data.get("region", "")}#/{data.get("resource", "")}',
            "apis": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/home?region={data.get("region", "")}\
                    #/{data.get("resource", "")}/resources/',
            "stage": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/\
                        home?region={data.get("region", "")}#/{data.get("resource", "")}',
            "certificate": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/home?region={data.get("region", "")}\
                    #/{data.get("resource", "")}/resources/',
            "resource": 'https://{data.get("region", "")}.{data.get("console", "")}/apigateway/home?region={data.get("region", "")}\
                    #/{data.get("resource", "")}/resources/',
        },
        "appconfig": {  # AWS AppConfig
            "application": 'https://{data.get("region", "")}.{data.get("console", "")}/systems-manager/appconfig/home?region={data.get("region", "")}',
            "deploymentstrategy": 'https://{data.get("region", "")}.{data.get("console", "")}/systems-manager/appconfig/home?region={data.get("region", "")}',
        },
        "appflow": {  # Amazon AppFlow
            "connectorprofile": 'https://{data.get("region", "")}.{data.get("console", "")}/appflow/home?region={data.get("region", "")}',
            "flow": 'https://{data.get("region", "")}.{data.get("console", "")}/appflow/home?region={data.get("region", "")}#/flows/{data.get("resource", "")}',
        },
        "appmesh": {  # AWS App Mesh
            "mesh": 'https://{data.get("region", "")}.{data.get("console", "")}/appmesh/home?region={data.get("region", "")}#/meshes/{data.get("resource", "")}',
        },
        "appmesh-preview": {  # AWS App Mesh Preview
            "mesh": 'https://{data.get("region", "")}.{data.get("console", "")}/appmesh/home?region={data.get("region", "")}#/meshes/{data.get("resource", "")}',
        },
        "appstream": {  # Amazon AppStream 2.0
            "fleet": 'https://{data.get("region", "")}.{data.get("console", "")}/appstream2/home?region={data.get("region", "")}#/fleets/{data.get("resource", "")}',
            "image": 'https://{data.get("region", "")}.{data.get("console", "")}/appstream2/home?region={data.get("region", "")}#/images',
            "image-builder": 'https://{data.get("region", "")}.{data.get("console", "")}/appstream2/home?region={data.get("region", "")}#/imageBuilders',
            "stack": 'https://{data.get("region", "")}.{data.get("console", "")}/appstream2/home?region={data.get("region", "")}#/stacks/{data.get("resource", "")}',
        },
        "appsync": {  # AWS AppSync
            "apis": 'https://{data.get("region", "")}.{data.get("console", "")}/appsync/home?region={data.get("region", "")}#/{data.get("resource", "")}',
        },
        "artifact": {  # AWS Artifact
            "agreement": None,
            "customer-agreement": None,
            "report-package": None,
        },
        "athena": {  # Amazon Athena
            "datacatalog": 'https://{data.get("region", "")}.{data.get("console", "")}/athena/home?region={data.get("region", "")}#/data-sources/catalog/{data.get("resource", "")}',
            "workgroup": 'https://{data.get("region", "")}.{data.get("console", "")}/athena/home?region={data.get("region", "")}#/workgroups/details/{data.get("resource", "")}',
        },
        "autoscaling": {  # Amazon EC2 Auto Scaling
            "autoScalingGroup": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#AutoScalingGroupDetails:id={data.get("resource", "")}',
            "launchConfiguration": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#LaunchConfigurations:',
        },
        "aws-marketplace": {  # AWS Marketplace Catalog
        },
        "backup": {  # AWS Backup
            "backup-plan": 'https://{data.get("region", "")}.{data.get("console", "")}/backup/home?region={data.get("region", "")}#/backupplan/details/{data.get("resource", "")}',
            "backup-vault": 'https://{data.get("region", "")}.{data.get("console", "")}/backup/home?region={data.get("region", "")}#/backupvault/details/{data.get("resource", "")}',
        },
        "batch": {  # AWS Batch
            "job-definition": 'https://{data.get("region", "")}.{data.get("console", "")}/batch/home?region={data.get("region", "")}#job-definition/detail/{data.get("resource", "")}',
            "job-queue": 'https://{data.get("region", "")}.{data.get("console", "")}/batch/home?region={data.get("region", "")}#queues/detail/{data.get("resource", "")}',
        },
        "bedrock": {  # Amazon Bedrock
            "agent": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/agents/{data.get("resource", "")}',
            "agent-alias": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/agents/{data.get("resource", "")}',
            "custom-model": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/custom-models/{data.get("resource", "")}',
            "evaluation-job": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/evaluations/{data.get("resource", "")}',
            "flow": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/flows/{data.get("resource", "")}',
            "foundation-model": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/foundation-models/{data.get("resource", "")}',
            "guardrail": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/guardrails/{data.get("resource", "")}',
            "inference-profile": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/inference-profiles/{data.get("resource", "")}',
            "knowledge-base": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/knowledge-bases/{data.get("resource", "")}',
            "model-customization-job": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/custom-models/jobs/{data.get("resource", "")}',
            "provisioned-model": 'https://{data.get("region", "")}.{data.get("console", "")}/bedrock/home?region={data.get("region", "")}#/provisioned-throughput/{data.get("resource", "")}',
        },
        "budgets": {  # AWS Budget Service
            "budget": 'https://{data.get("console", "")}/billing/home?#/budgets/budget/{data.get("resource", "")}',
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
            "environment": 'https://{data.get("region", "")}.{data.get("console", "")}/cloud9/home/environments/{data.get("resource", "")}?region={data.get("region", "")}',
        },
        "clouddirectory": {  # Amazon Cloud Directory
            "directory": None,
            "schema": None,
        },
        "cloudformation": {  # AWS CloudFormation
            "changeSet": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudformation/home?region={data.get("region", "")}#/stacks',
            "stack": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudformation/home?region={data.get("region", "")}\
            #/stacks/stackinfo?stackId={arn}&# filteringStatus=active&filteringText=&viewNested=true&hideStacks=false',
            "stackset": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudformation/home?region={data.get("region", "")}#/stacksets/{data.get("resource", "")}/stacks',
        },
        "cloudfront": {  # Amazon CloudFront
            "distribution": 'https://{data.get("console", "")}/cloudfront/v4/home#/{data.get("resource", "")}',
            "origin-access-identity": 'https://{data.get("console", "")}/cloudfront/v4/home#/origin-access',
            "streaming-distribution": None,
        },
        "cloudhsm": {  # AWS CloudHSM
            "backup": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudhsm/home?region={data.get("region", "")}#/backups',
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudhsm/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}',
        },
        "cloudsearch": {  # Amazon CloudSearch
            "domain": None,
        },
        "cloudtrail": {  # AWS CloudTrail
            "trail": 'https://{data.get("console", "")}/cloudtrail/home?region={data.get("region", "")}#/trails/\
            {data.get("resource", "")}',
        },
        "cloudwatch": {  # Amazon CloudWatch
            "alarm": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#alarmsV2:alarm/{data.get("resource", "")}?',
            "metrics": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#metricsV2:graph=~()',
            "loggroup": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?\
                    region={data.get("region", "")}#logsV2:log-groups/{data.get("resource", "")}',
            "flowlog": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?\
                    region={data.get("region", "")}#logsV2:log-groups/{data.get("resource", "")}',
            "dashboard": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#dashboards/dashboard/{data.get("resource", "")}',
            "insight-rule": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#contributor-insights:',
            "event-bus": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#eventbuses:',
            "rule": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region=u{data.get("region", "")}#rules:',
        },
        "codeartifact": {  # AWS CodeArtifact
            "domain": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codeartifact/domains/{data.get("resource", "")}?region={data.get("region", "")}',
            "package": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codeartifact/packages?region={data.get("region", "")}',
            "repository": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codeartifact/repositories/{data.get("resource", "")}?region={data.get("region", "")}',
        },
        "codebuild": {  # AWS CodeBuild
            "build": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codebuild/projects?region={data.get("region", "")}',
            "project": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codebuild/{data.get("account", "")}/projects/{data.get("resource", "")}/history?region={data.get("region", "")}',
            "report": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codebuild/testReports/reports?region={data.get("region", "")}',
            "report-group": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codebuild/testReports/reportGroups/{data.get("resource", "")}?region={data.get("region", "")}',
        },
        "codecommit": {  # Amazon CodeGuru Reviewer
        },
        "codedeploy": {  # AWS CodeDeploy
            "application": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codedeploy/applications/{data.get("resource", "")}?region={data.get("region", "")}',
            "deploymentconfig": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codedeploy/deployment-configurations?region={data.get("region", "")}',
            "deploymentgroup": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codedeploy/applications?region={data.get("region", "")}',
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
            "actiontype": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codepipeline/action-types?region={data.get("region", "")}',
            "webhook": 'https://{data.get("region", "")}.{data.get("console", "")}/codesuite/codepipeline/webhooks?region={data.get("region", "")}',
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
            "identitypool": 'https://{data.get("region", "")}.{data.get("console", "")}/cognito/v2/identity/identity-pools/{data.get("resource", "")}/basic-information?region={data.get("region", "")}',
        },
        "cognito-idp": {  # Amazon Cognito User Pools
            "userpool": 'https://{data.get("region", "")}.{data.get("console", "")}/cognito/v2/idp/user-pools/{data.get("resource", "")}/users?region={data.get("region", "")}',
        },
        "cognito-sync": {  # Amazon Cognito Sync
            "identitypool": 'https://{data.get("region", "")}.{data.get("console", "")}/cognito/v2/identity/identity-pools/{data.get("resource", "")}/basic-information?region={data.get("region", "")}',
        },
        "comprehend": {  # Amazon Comprehend
            "document-classifier": None,
            "document-classifier-endpoint": None,
            "entity-recognizer": None,
        },
        "config": {  # AWS Config
            "aggregation-authorization": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/aggregations',
            "config-aggregator": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/aggregations',
            "config-rule": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/rules/rule-details/{data.get("resource", "")}',
            "conformance-pack": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/conformance-packs/details/{data.get("resource", "")}',
            "organization-config-rule": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/rules',
            "organization-conformance-pack": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/conformance-packs',
            "remediation-configuration": 'https://{data.get("region", "")}.{data.get("console", "")}/config/home?region={data.get("region", "")}#/rules',
        },
        "connect": {  # Amazon Connect
            "instance": 'https://{data.get("region", "")}.{data.get("console", "")}/connect/home?region={data.get("region", "")}',
        },
        "cur": {  # AWS Cost and Usage Report
            "definition": None,
        },
        "dataexchange": {  # AWS Data Exchange
            "data-sets": None,
            "jobs": None,
        },
        "datasync": {  # DataSync
            "agent": 'https://{data.get("region", "")}.{data.get("console", "")}/datasync/home?region={data.get("region", "")}#/agents/{data.get("resource", "")}',
            "location": 'https://{data.get("region", "")}.{data.get("console", "")}/datasync/home?region={data.get("region", "")}#/locations/{data.get("resource", "")}',
            "task": 'https://{data.get("region", "")}.{data.get("console", "")}/datasync/home?region={data.get("region", "")}#/tasks/{data.get("resource", "")}',
        },
        "dax": {  # Amazon DynamoDB Accelerator (DAX)
            "cache": 'https://{data.get("region", "")}.{data.get("console", "")}/dynamodbv2/home?region={data.get("region", "")}#dax:cluster-details:{data.get("resource", "")}',
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
            "dx-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/directconnect/v2/home?region={data.get("region", "")}#/direct-connect-gateways/{data.get("resource", "")}',
            "dxcon": 'https://{data.get("region", "")}.{data.get("console", "")}/directconnect/v2/home?region={data.get("region", "")}#/connections/{data.get("resource", "")}',
            "dxlag": 'https://{data.get("region", "")}.{data.get("console", "")}/directconnect/v2/home?region={data.get("region", "")}#/lags/{data.get("resource", "")}',
            "dxvif": 'https://{data.get("region", "")}.{data.get("console", "")}/directconnect/v2/home?region={data.get("region", "")}#/virtual-interfaces/{data.get("resource", "")}',
        },
        "dlm": {  # Amazon Data Lifecycle Manager
            "policy": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#LifecyclePolicies:',
        },
        "dms": {  # AWS Database Migration Service
            "cert": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#certificates',
            "endpoint": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#endpointDetails/{data.get("resource", "")}',
            "es": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#eventSubscriptions',
            "rep": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#replicationInstanceDetails/{data.get("resource", "")}',
            "subgrp": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#subnetGroupDetails/{data.get("resource", "")}',
            "task": 'https://{data.get("region", "")}.{data.get("console", "")}/dms/v2/home?region={data.get("region", "")}#taskDetails/{data.get("resource", "")}',
        },
        "ds": {  # AWS Directory Service
            "directory": 'https://{data.get("region", "")}.{data.get("console", "")}/directoryservicev2/home?region={data.get("region", "")}#/directories/{data.get("resource", "")}',
        },
        "dynamodb": {  # Amazon DynamoDB
            "global-table": 'https://{data.get("region", "")}.{data.get("console", "")}/dynamodbv2/home?region={data.get("region", "")}#table?name={data.get("resource", "")}',
            "table": 'https://{data.get("region", "")}.{data.get("console", "")}/dynamodbv2/home?region=\
                {data.get("region", "")}#table?name={data.get("resource", "")}',
            "secondary_indexes": 'https://{data.get("region", "")}.{data.get("console", "")}/dynamodbv2/\
                                home?region=us-east-1#table?initialTagKey=&name={data.get("resource", "")}&tab=indexes',
        },
        "ec2": {  # AWS Systems Manager
            "capacity-reservation": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#CapacityReservationDetails:capacityReservationId={data.get("resource", "")}',
            "client-vpn-endpoint": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#ClientVPNEndpoints:',
            "customer-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#CustomerGateways:',
            "dedicated-host": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#Hosts:',
            "dhcp-options": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#DHCPOptions:dhcpOptionsId={data.get("resource", "")}',
            "elastic-gpu": None,
            "fpga-image": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#FpgaImages:',
            "image": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get("region", "")}#ImageDetails:imageId={data.get("resource", "")}',
            "instance": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get\
                ("region", "")}#InstanceDetails:instanceId={data.get("resource", "")}',
            "internet-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#InternetGateway:internetGatewayId={data.get("resource", "")}',
            "key-pair": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/v2/home?region={data.get\
                ("region", "")}#KeyPairs:',
            "launch-template": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#LaunchTemplateDetails:launchTemplateId={data.get("resource", "")}',
            "local-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#LocalGateways:',
            "local-gateway-route-table": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#LocalGatewayRouteTables:',
            "local-gateway-route-table-virtual-interface-group-association": None,
            "local-gateway-route-table-vpc-association": None,
            "local-gateway-virtual-interface": None,
            "local-gateway-virtual-interface-group": None,
            "network-acl": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#NetworkAcls:networkAclId={data.get("resource", "")}',
            "network-interface": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                    home?region={data.get("region", "")}#NetworkInterface:networkInterfaceId={data.get("resource", "")}',
            "placement-group": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#PlacementGroups:',
            "reserved-instances": 'https://{data.get("region", "")}.{data.get("console", "")}/\
                    ec2/home?region={data.get("region", "")}#ReservedInstances:',
            "route-table": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#RouteTables:routeTableId={data.get("resource", "")}',
            "security-group": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SecurityGroup:groupId={data.get("resource", "")}',
            "snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?\
                    region={data.get("region", "")}#SnapshotDetails:snapshotId={data.get("resource", "")}',
            "spot-instances-request": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#SpotInstances:',
            "subnet": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SubnetDetails:subnetId={data.get("resource", "")}',
            "traffic-mirror-filter": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TrafficMirrorFilters:',
            "traffic-mirror-filter-rule": None,
            "traffic-mirror-session": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TrafficMirrorSessions:',
            "traffic-mirror-target": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TrafficMirrorTargets:',
            "transit-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TransitGateways:transitGatewayId={data.get("resource", "")}',
            "transit-gateway-attachment": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TransitGatewayAttachments:',
            "transit-gateway-multicast-domain": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TransitGatewayMulticastDomains:',
            "transit-gateway-route-table": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#TransitGatewayRouteTables:',
            "volume": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2\
                    /home?region={data.get("region", "")}#VolumeDetails:volumeId={data.get("resource", "")}',
            "vpc": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#VpcDetails:VpcId={data.get("resource", "")}',
            "vpc-endpoint": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#Endpoints:vpcEndpointId={data.get("resource", "")}',
            "vpc-endpoint-service": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#EndpointServices:',
            "vpc-flow-log": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region={data.get("region", "")}#subnets:',
            "vpc-peering-connection": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#PeeringConnections:vpcPeeringConnectionId={data.get("resource", "")}',
            "vpn-connection": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#VpnConnections:vpnConnectionId={data.get("resource", "")}',
            "vpn-gateway": 'https://{data.get("region", "")}.{data.get("console", "")}/vpcconsole/home?region={data.get("region", "")}#VpnGateways:',
            "elastic-ip": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                    home?region={data.get("region", "")}#ElasticIpDetails:AllocationId={data.get("resource", "")}',
            "beanstalk_environment": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/\
                    home?region={data.get("region", "")}#/environment/dashboard?environmentId={data.get("resource", "")}',
            "loadbalancer": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                            home?region=u{data.get("region", "")}#LoadBalancers:search={data.get("resource", "")};sort=loadBalancerName',
        },
        "ecr": {  # Amazon Elastic Container Registry
            "repository": 'https://{data.get("region", "")}.{data.get("console", "")}/ecr/repositories/{data.get\
                ("resource", "")}?region={data.get("region", "")}',
            "image": 'https://{data.get("region", "")}.{data.get("console", "")}/ecr/repositories/{data.get\
                ("resource", "")}?region={data.get("region", "")}',
        },
        "ecs": {  # Amazon Elastic Container Service
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}',
            "container-instance": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}/containerInstances',
            "service": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}/services',
            "task": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}/tasks',
            "task-definition": 'https://{data.get("region", "")}.{data.get("console", "")}/ecs\
                    /home?region={data.get("region", "")}#/taskDefinitions/{data.get("resource", "")}',
            "task-set": None,  # task-set is a sub-resource of service, no direct deep-link
        },
        "eks": {  # Amazon Elastic Container Service for Kubernetes
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/eks/home?region={data.get\
                ("region", "")}#/clusters/{data.get("resource", "")}',
            "fargateprofile": 'https://{data.get("region", "")}.{data.get("console", "")}/eks/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}/fargate-profiles',
            "nodegroup": 'https://{data.get("region", "")}.{data.get("console", "")}/eks/home?region={data.get("region", "")}#/clusters/{data.get("resource", "")}/nodegroups',
        },
        "elastic-inference": {  # Amazon Elastic Inference
            "elastic-inference-accelerator": None,
        },
        "elasticbeanstalk": {  # AWS Elastic Beanstalk
            "application": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/home?region={data.get("region", "")}#/application/overview?applicationName={data.get("resource", "")}',
            "applicationversion": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/home?region={data.get("region", "")}#/application/versions?applicationName={data.get("resource", "")}',
            "configurationtemplate": None,  # no direct deep-link; sub-resource of application
            "environment": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/home?region={data.get("region", "")}#/environment/dashboard?environmentId={data.get("resource", "")}',
            "platform": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticbeanstalk/home?region={data.get("region", "")}#/platforms',
            "solutionstack": None,  # internal resource, not directly navigable
        },
        "elasticfilesystem": {  # Amazon Elastic File System
            "access-point": 'https://{data.get("region", "")}.{data.get("console", "")}/efs/home?region={data.get("region", "")}#/access-points/{data.get("resource", "")}',
            "file-system": 'https://{data.get("region", "")}.{data.get("console", "")}/efs/home?region={data.get("region", "")}#/file-systems/{data.get("resource", "")}',
        },
        "elasticloadbalancing": {  # AWS WAF V2
            "listener": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#LoadBalancers:',
            "listener-rule": None,  # sub-resource of listener, no direct deep-link
            "loadbalancer": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/\
                        home?region={data.get("region", "")}#LoadBalancers:sort=loadBalancerName',
            "targetgroup": 'https://{data.get("region", "")}.{data.get("console", "")}/ec2/home?region={data.get("region", "")}#TargetGroups:targetGroupArn={arn}',
        },
        "elasticmapreduce": {  # Amazon Elastic MapReduce
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticmapreduce/home?region={data.get("region", "")}#cluster-details:{data.get("resource", "")}',
            "editor": 'https://{data.get("region", "")}.{data.get("console", "")}/elasticmapreduce/home?region={data.get("region", "")}#/notebooks',
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
                        home?region={data.get("region", "")}#opensearch/reserved-instances',
        },
        "events": {  # Amazon EventBridge
            "event-bus": 'https://{data.get("region", "")}.{data.get("console", "")}/events/home?region={data.get("region", "")}#/eventbus/{data.get("resource", "")}',
            "event-source": 'https://{data.get("region", "")}.{data.get("console", "")}/events/home?region={data.get("region", "")}#/partner-event-sources',
            "rule": 'https://{data.get("region", "")}.{data.get("console", "")}/events/home?region={data.get("region", "")}#/rules/{data.get("resource", "")}',
        },
        "execute-api": {  # Amazon API Gateway
        },
        "firehose": {  # Amazon Kinesis Firehose
            "deliverystream": 'https://{data.get("region", "")}.{data.get("console", "")}/firehose/home?region={data.get("region", "")}#/details/{data.get("resource", "")}/monitoring',
        },
        "fms": {  # AWS Firewall Manager
            "policy": 'https://{data.get("console", "")}/wafv2/fmsv2/home?region={data.get("region", "")}#/security-policies/{data.get("resource", "")}',
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
            "backup": 'https://{data.get("region", "")}.{data.get("console", "")}/fsx/home?region={data.get("region", "")}#backups',
            "file-system": 'https://{data.get("region", "")}.{data.get("console", "")}/fsx/home?region={data.get("region", "")}#file-systems/{data.get("resource", "")}',
            "task": 'https://{data.get("region", "")}.{data.get("console", "")}/fsx/home?region={data.get("region", "")}#data-repository-tasks',
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
            "catalog": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/data-catalog/databases',
            "connection": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/data-connections/{data.get("resource", "")}/details',
            "crawler": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/data-catalog/crawlers/{data.get("resource", "")}',
            "database": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/data-catalog/databases/view/{data.get("resource", "")}',
            "devendpoint": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/dev-endpoint/{data.get("resource", "")}',
            "job": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/etl/jobs/{data.get("resource", "")}',
            "mlTransform": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/ml-transforms/{data.get("resource", "")}',
            "table": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/data-catalog/tables',
            "tableVersion": None,  # sub-resource of table, no direct deep-link
            "trigger": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/etl/triggers/{data.get("resource", "")}',
            "userDefinedFunction": None,  # accessible only through database view
            "workflow": 'https://{data.get("region", "")}.{data.get("console", "")}/glue/home?region={data.get("region", "")}#/etl/workflows/{data.get("resource", "")}',
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
            "detector": 'https://{data.get("region", "")}.{data.get("console", "")}/guardduty/home?region={data.get("region", "")}#/',
        },
        "health": {  # AWS Health APIs and Notifications
            "event": None,
        },
        "honeycode": {  # Amazon Honeycode
            "screen": None,
            "screen-automation": None,
        },
        "iam": {  # AWS Security Token Service
            "access-report": 'https://{data.get("console", "")}/iamv2/home#/last-access-details',
            "assumed-role": None,  # no direct console page for assumed role
            "federated-user": None,  # transient identity, no console page
            "group": 'https://{data.get("console", "")}/iamv2/home#/groups/details/{get_resource_path\
            (data.get("resource", ""))}',
            "instance-profile": 'https://{data.get("console", "")}/iamv2/home#/roles/{data.get("resource", "")}',
            "mfa": 'https://{data.get("console", "")}/iam/home?#/users/{data.get("resource", "")}?section=security_credentials',
            "oidc-provider": 'https://{data.get("console", "")}/iam/home?#/providers/{get_arn_string(data)}',
            "policy": 'https://{data.get("console", "")}/iam/home?#/policies/{get_arn_string(data)}',
            "role": 'https://{data.get("console", "")}/iam/home?#/roles/{get_resource_path(data.get("resource", ""))}',
            "saml-provider": 'https://{data.get("console", "")}/iamv2/home#/identity-providers',
            "server-certificate": 'https://{data.get("console", "")}/iam/home?#/server-certificates',
            "sms-mfa": None,  # no direct console deep-link for SMS MFA device
            "user": 'https://{data.get("console", "")}/iam/home?#/users/{data.get("resource", "")}',
            "access_keys": 'https://{data.get("console", "")}/iam/home#/users/{data.get("resource", "")}?section=security_credentials',
            "policy_statement": 'https://{data.get("console", "")}/iam/home?#/policies/{get_arn_string(data)}',
        },
        "imagebuilder": {  # Amazon EC2 Image Builder
            "component": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/components/{data.get("resource", "")}',
            "distribution-configuration": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/distributionSettings/{data.get("resource", "")}',
            "image": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/images/{data.get("resource", "")}',
            "image-pipeline": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/pipelines/{data.get("resource", "")}',
            "image-recipe": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/imageRecipes/{data.get("resource", "")}',
            "infrastructure-configuration": 'https://{data.get("region", "")}.{data.get("console", "")}/imagebuilder/home?region={data.get("region", "")}#/infrastructureConfiguration/{data.get("resource", "")}',
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
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/msk/home?region={data.get("region", "")}#/cluster/{data.get("resource", "")}/view',
        },
        "kendra": {  # Amazon Kendra
            "index": 'https://{data.get("region", "")}.{data.get("console", "")}/kendra/home?region={data.get("region", "")}#indexes/{data.get("resource", "")}',
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
            "alias": 'https://{data.get("region", "")}.{data.get("console", "")}/kms/home?region={data.get("region", "")}#/kms/aliases',
            "key": 'https://{data.get("region", "")}.{data.get("console", "")}/kms/\
                    home?region={data.get("region", "")}#/kms/keys/{data.get("resource", "")}',
        },
        "lambda": {  # AWS Lambda
            "event-source-mapping": 'https://{data.get("region", "")}.{data.get("console", "")}/lambda/home?region=\
                {data.get("region", "")}#/functions/{data.get("resource", "")}',
            "function": 'https://{data.get("region", "")}.{data.get("console", "")}/lambda/home?region=\
                {data.get("region", "")}#/functions/{data.get("resource", "")}',
            "alias": 'https://{data.get("region", "")}.{data.get("console", "")}/lambda/\
                        home?region={data.get("region", "")}#/functions/{data.get("resource", "")}?tab=aliases',
            "layer": 'https://{data.get("region", "")}.{data.get("console", "")}/lambda/home?region=\
                {data.get("region", "")}#/functions/{data.get("resource", "")}',
        },
        "lex": {  # Amazon Lex
            "bot": 'https://{data.get("region", "")}.{data.get("console", "")}/lex/home?region={data.get("region", "")}#bot/{data.get("resource", "")}',
            "bot-channel": None,  # sub-resource of bot, no direct deep-link
            "intent": None,  # sub-resource of bot, no direct deep-link
            "slottype": None,  # sub-resource of bot, no direct deep-link
        },
        "license-manager": {  # AWS License Manager
            "license-configuration": 'https://{data.get("region", "")}.{data.get("console", "")}/license-manager/home?region={data.get("region", "")}#licenseConfigurationDetail/{data.get("resource", "")}',
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
            "log-group": 'https://{data.get("region", "")}.{data.get("console", "")}/cloudwatch/home?region={data.get("region", "")}#logsV2:log-groups/log-group/{data.get("resource", "")}',
        },
        "machinelearning": {  # Amazon Machine Learning
            "batchprediction": None,
            "datasource": None,
            "evaluation": None,
            "mlmodel": None,
        },
        "macie2": {  # Amazon Macie
            "classification-job": 'https://{data.get("region", "")}.{data.get("console", "")}/macie/home?region={data.get("region", "")}#jobs/{data.get("resource", "")}',
            "custom-data-identifier": 'https://{data.get("region", "")}.{data.get("console", "")}/macie/home?region={data.get("region", "")}#custom-data-identifiers/details/{data.get("resource", "")}',
            "findings-filter": 'https://{data.get("region", "")}.{data.get("console", "")}/macie/home?region={data.get("region", "")}#findings/filters',
            "member": 'https://{data.get("region", "")}.{data.get("console", "")}/macie/home?region={data.get("region", "")}#accounts',
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
            "broker": 'https://{data.get("region", "")}.{data.get("console", "")}/amazon-mq/home?region={data.get("region", "")}#/brokers/{data.get("resource", "")}',
            "configuration": 'https://{data.get("region", "")}.{data.get("console", "")}/amazon-mq/home?region={data.get("region", "")}#/configurations/{data.get("resource", "")}',
        },
        "neptune-db": {  # Amazon Neptune
        },
        "networkmanager": {  # Network Manager
            "device": 'https://{data.get("console", "")}/networkmanager/home?region={data.get("region", "")}#/networks/{data.get("resource", "")}/devices',
            "global-network": 'https://{data.get("console", "")}/networkmanager/home?region={data.get("region", "")}#/networks/{data.get("resource", "")}',
            "link": 'https://{data.get("console", "")}/networkmanager/home?region={data.get("region", "")}#/networks/{data.get("resource", "")}/links',
            "site": 'https://{data.get("console", "")}/networkmanager/home?region={data.get("region", "")}#/networks/{data.get("resource", "")}/sites',
        },
        "opsworks": {  # AWS OpsWorks
            "stack": None,
        },
        "organizations": {  # AWS Organizations
            "account": 'https://{data.get("console", "")}/organizations/v2/home/accounts/{data.get("resource", "")}',
            "handshake": None,  # no direct console deep-link for handshakes
            "organization": 'https://{data.get("region", "")}.{data.get("console", "")}/organizations/v2/home/accounts/{data.get("resource", "")}',
            "ou": 'https://{data.get("console", "")}/organizations/v2/home/roots',
            "policy": 'https://{data.get("console", "")}/organizations/v2/home/policies/{data.get("resource", "")}',
            "root": 'https://{data.get("console", "")}/organizations/v2/home/roots',
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
            "ledger": 'https://{data.get("region", "")}.{data.get("console", "")}/qldb/home?region={data.get("region", "")}#/ledger/{data.get("resource", "")}',
            "stream": 'https://{data.get("region", "")}.{data.get("console", "")}/qldb/home?region={data.get("region", "")}#/ledger/{data.get("resource", "")}/streams',
        },
        "quicksight": {  # Amazon QuickSight
            "assignment": None,  # policy assignment, no direct deep-link
            "dashboard": 'https://{data.get("region", "")}.{data.get("console", "")}/quicksight/home?region={data.get("region", "")}#/dashboards',
            "group": 'https://{data.get("region", "")}.{data.get("console", "")}/quicksight/home?region={data.get("region", "")}#/admin/groups',
            "template": None,  # templates not directly browsable in console
            "user": 'https://{data.get("region", "")}.{data.get("console", "")}/quicksight/home?region={data.get("region", "")}#/admin/users',
        },
        "ram": {  # AWS Resource Access Manager
            "permission": 'https://{data.get("region", "")}.{data.get("console", "")}/ram/home?region={data.get("region", "")}#Permissions:',
            "resource-share": 'https://{data.get("region", "")}.{data.get("console", "")}/ram/home?region={data.get("region", "")}#ResourceShare:{data.get("resource", "")}',
            "resource-share-invitation": 'https://{data.get("region", "")}.{data.get("console", "")}/ram/home?region={data.get("region", "")}#ReceivedShares:',
        },
        "rds": {  # Amazon RDS
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/\
                    home?region={data.get("region", "")}#database:id={data.get("resource", "")};is-cluster=true',
            "cluster-endpoint": None,  # sub-resource of cluster, no direct deep-link
            "cluster-pg": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#cluster-parameter-groups:',
            "cluster-snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#cluster-snapshots:',
            "db": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region=\
                {data.get("region", "")}#database:id={data.get("resource", "")};is-cluster=false',
            "db-proxy": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#proxy:id={data.get("resource", "")}',
            "es": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#event-subscriptions:',
            "og": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#option-groups-list:',
            "pg": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#parameter-groups-list:',
            "ri": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#reserved-instances:',
            "secgrp": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SecurityGroup:groupId={data.get("resource", "")}',
            "snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#db-snapshot:engine=sqlserver-ee;id={arn}',
            "subgrp": 'https://{data.get("region", "")}.{data.get("console", "")}/rds/home?region={data.get("region", "")}#subnet-groups-list:',
            "target": None,  # sub-resource of db-proxy, no direct deep-link
            "target-group": None,  # sub-resource of db-proxy, no direct deep-link
        },
        "rds-db": {  # Amazon RDS IAM Authentication
            "dbuser": None,
        },
        "redshift": {  # Amazon Redshift
            "cluster": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region=\
                {data.get("region", "")}#cluster-details?cluster={data.get("resource", "")}',
            "dbgroup": None,  # database group, accessible only through SQL, no UI deep-link
            "dbname": None,  # internal resource, no direct console page
            "dbuser": None,  # internal resource, no direct console page
            "eventsubscription": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region={data.get("region", "")}#event-subscriptions',
            "hsmclientcertificate": None,  # legacy HSM feature, limited console support
            "hsmconfiguration": None,  # legacy HSM feature, limited console support
            "parametergroup": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region={data.get("region", "")}#parameter-groups',
            "securitygroup": 'https://{data.get("region", "")}.{data.get("console", "")}/vpc/home?region=\
                {data.get("region", "")}#SecurityGroup:groupId={data.get("resource", "")}',
            "securitygroupingress": None,  # sub-resource of security group, no direct deep-link
            "snapshot": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region={data.get("region", "")}#snapshots',
            "snapshotcopygrant": None,  # internal resource, no direct console page
            "snapshotschedule": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region={data.get("region", "")}#snapshot-schedules',
            "subnetgroup": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2/home?region={data.get("region", "")}#subnet-groups',
            "reserved-node": 'https://{data.get("region", "")}.{data.get("console", "")}/redshiftv2\
                        /home?region={data.get("region", "")}#reserved-nodes',
        },
        "rekognition": {  # Amazon Rekognition
            "collection": 'https://{data.get("region", "")}.{data.get("console", "")}/rekognition/home?region={data.get("region", "")}#/',
            "project": 'https://{data.get("region", "")}.{data.get("console", "")}/rekognition/home?region={data.get("region", "")}#/projects/{data.get("resource", "")}',
            "streamprocessor": 'https://{data.get("region", "")}.{data.get("console", "")}/rekognition/home?region={data.get("region", "")}#/stream-processors',
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
            "domains": 'https://{data.get("region", "")}.{data.get("console", "")}/route53/home#DomainListing:',
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
            "algorithm": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/algorithms/{data.get("resource", "")}',
            "app": None,
            "automl-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/auto-ml/{data.get("resource", "")}',
            "code-repository": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/repositories/{data.get("resource", "")}',
            "compilation-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/compilation-jobs/{data.get("resource", "")}',
            "domain": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/studio/{data.get("resource", "")}',
            "endpoint": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/endpoints/{data.get("resource", "")}',
            "endpoint-config": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/endpointConfig/{data.get("resource", "")}',
            "experiment": None,
            "experiment-trial": None,
            "experiment-trial-component": None,
            "flow-definition": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/human-review-workflows/{data.get("resource", "")}',
            "human-loop": None,
            "human-task-ui": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/worker-task-templates/{data.get("resource", "")}',
            "hyper-parameter-tuning-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/hyper-tuning-jobs/{data.get("resource", "")}',
            "labeling-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/labeling-jobs/{data.get("resource", "")}',
            "model": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/models/{data.get("resource", "")}',
            "model-package": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/model-packages/{data.get("resource", "")}',
            "monitoring-schedule": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/monitoring-schedules/{data.get("resource", "")}',
            "notebook-instance": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/notebook-instances/{data.get("resource", "")}',
            "notebook-instance-lifecycle-config": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/notebook-lifecycle-config/{data.get("resource", "")}',
            "processing-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/processing-jobs/{data.get("resource", "")}',
            "training-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/jobs/{data.get("resource", "")}',
            "transform-job": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/transform-jobs/{data.get("resource", "")}',
            "user-profile": 'https://{data.get("region", "")}.{data.get("console", "")}/sagemaker/home?region={data.get("region", "")}#/studio/{data.get("resource", "")}',
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
            "topic": 'https://{data.get("region", "")}.{data.get("console", "")}/sns/v3/home?region={data.get("region", "")}#/topic/{arn}',
            "subscription": 'https://{data.get("region", "")}.{data.get("console", "")}/sns/v3/home?region={data.get("region", "")}#/subscription/{arn}',
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
