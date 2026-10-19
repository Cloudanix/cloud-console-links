import pytest

from cloudconsolelink.clouds.aws import AWSLinker
from cloudconsolelink.clouds.aws import ARNTooShortError
from cloudconsolelink.clouds.aws import InvalidARNError
from cloudconsolelink.clouds.aws import InvalidPartitionError
from cloudconsolelink.clouds.aws import InvalidServiceError
from cloudconsolelink.clouds.aws import get_service_home_link
from cloudconsolelink.clouds.aws import _render
from cloudconsolelink.clouds.aws.links import get_links

aws = AWSLinker()


def test_aws_ec2_instance():
    arn = "arn:aws:ec2:us-east1:1234567890:instance/instance1"
    expected_link = "https://us-east1.console.aws.amazon.com/ec2/v2/\
        home?region=us-east1#InstanceDetails:instanceId=instance1"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_ecr_repository():
    arn = "arn:aws:ecr:us-east1:1234567890:repository/repo1"
    expected_link = "https://us-east1.console.aws.amazon.com/ecr/repositories/private/1234567890/repo1\
        ?region=us-east1"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_eks_cluster():
    arn = "arn:aws:eks:us-east-2:1234567890:cluster/testing-cluster"
    expected_link = "https://us-east-2.console.aws.amazon.com/eks/home?region=\
        us-east-2#/clusters/testing-cluster"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_appflow_flow():
    arn = "arn:aws:appflow:us-east-2:123456789012:flow/FlowName-123"
    expected_link = (
        "https://us-east-2.console.aws.amazon.com/appflow/home?"
        "region=us-east-2#/flows/FlowName-123"
    )

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_appmesh_mesh():
    arn = "arn:aws:appmesh:us-east-2:123456789012:mesh/MyMesh"
    expected_link = (
        "https://us-east-2.console.aws.amazon.com/appmesh/home?"
        "region=us-east-2#/meshes/MyMesh"
    )

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_bedrock_agent():
    arn = "arn:aws:bedrock:us-east-2:123456789012:agent/agent-123"
    expected_link = (
        "https://us-east-2.console.aws.amazon.com/bedrock/home?"
        "region=us-east-2#/agents/agent-123"
    )

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_rds_db_instance():
    arn = "arn:aws:rds:us-east-2:123456789012:db:my-mysql-instance-1"
    expected_link = "https://us-east-2.console.aws.amazon.com/rds/home?region=\
        us-east-2#database:id=my-mysql-instance-1;is-cluster=false"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_redshift_cluster():
    arn = "arn:aws:redshift:us-east-2:123456789012:cluster:my-mysql-instance-1"
    expected_link = "https://us-east-2.console.aws.amazon.com/redshiftv2/home?region=\
        us-east-2#cluster-details?cluster=my-mysql-instance-1"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_cloudwatch_alerm():
    arn = "arn:aws:cloudwatch:us-east-2:123456789012:alarm:AlarmName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#alarmsV2:alarm/AlarmName-123?'
    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_cloudformation_stack():
    arn = "arn:aws:cloudformation:us-east-2:123456789012:stack/stackName-123/stack123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2\
            #/stacks/stackinfo?stackId=arn:aws:cloudformation:us-east-2:123456789012:stack/stackName-123/stack123&# filteringStatus=active&filteringText=&viewNested=true&hideStacks=false'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_cloudtrail_trail():
    arn = "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/cloudtrail/home?region=us-east-2\
    #/trails/arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName-123'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_cloudwatch_alerm():
    arn = "arn:aws:cloudwatch:us-east-2:123456789012:alarm/c"
    expected_link = 'https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2\
    #alarmsV2:alarm/c?'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_event_eventbus():
    arn = "arn:aws:events:us-east-2:123456789012:event-bus/EventBusName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/events/home?region=us-east-2#/eventbus/EventBusName-123'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_event_rule():
    arn = "arn:aws:events:us-east-2:123456789012:rule/RuleName-123"
    expected_link = "https://us-east-2.console.aws.amazon.com/events/home?region=us-east-2#/rules/RuleName-123"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_cloudwatch_rule():
    arn = "arn:aws:cloudwatch:us-east-2:123456789012:rule/RuleName-123"
    expected_link = "https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#rules:"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_apigateway_client_certificate():
    arn = "arn:aws:apigateway:us-east-1::clientcertificates/abc123"
    expected_link = "https://us-east-1.console.aws.amazon.com/apigateway/home?region=us-east-1#/client-certificates"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link


def test_aws_apigateway_documented_arns_with_leading_slash():
    # AWS documents API Gateway ARNs as paths (::/restapis/...). Before: the "/" left an empty
    # resource type, so every one fell back to the API Gateway home page. The classic #/{id} console
    # paths are gone, so REST APIs link to /apigateway/main/apis and HTTP APIs to api-detail.
    home = "https://us-east-1.console.aws.amazon.com/apigateway/home?region=us-east-1"
    main = "https://us-east-1.console.aws.amazon.com/apigateway/main"
    cases = {
        "arn:aws:apigateway:us-east-1::/restapis/abc123": f"{main}/apis/abc123/resources?api=abc123&region=us-east-1",
        "arn:aws:apigateway:us-east-1::/restapis/abc123/stages/prod": (
            f"{main}/apis/abc123/stages?api=abc123&region=us-east-1"
        ),
        "arn:aws:apigateway:us-east-1::/restapis/abc123/resources/r1": (
            f"{main}/apis/abc123/resources?api=abc123&region=us-east-1"
        ),
        "arn:aws:apigateway:us-east-1::/apis/abc123": f"{main}/api-detail?api=abc123&region=us-east-1",
        "arn:aws:apigateway:us-east-1::/clientcertificates/abc123": f"{home}#/client-certificates",
    }
    for arn, expected_link in cases.items():
        assert aws.get_console_link(arn=arn) == expected_link
        # Same link as the slash-less form callers send today.
        assert aws.get_console_link(arn=arn.replace("::/", "::")) == expected_link


def test_aws_route53_domain_has_no_region_host():
    # Before: the empty region produced the host "https://.console.aws.amazon.com".
    arn = "arn:aws:route53:::domains/example.com"

    assert aws.get_console_link(arn=arn) == "https://console.aws.amazon.com/route53/home#DomainListing:"
    assert (
        aws.get_console_link(arn="arn:aws-us-gov:route53:::domains/example.com")
        == "https://console.amazonaws-us-gov.com/route53/home#DomainListing:"
    )


def test_aws_cloudwatch_loggroup():
    arn = "arn:aws:logs:us-east-2:123456789012:log-group/LogGroupName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#logsV2:log-groups/log-group/LogGroupName-123'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_ses_identity():
    arn = "arn:aws:ses:us-east-2:123456789012:identity/IdentityName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/ses/home?region=us-east-2\
        #/verified-identities/IdentityName-123'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_sns_topic():
    arn = "arn:aws:sns:us-east-2:123456789012:TopicName-123"
    expected_link = 'https://us-east-2.console.aws.amazon.com/sns/v3/home?region=us-east-2#/topic/arn:aws:sns:us-east-2:123456789012:TopicName-123'

    out_link = aws.get_console_link(arn=arn)
    print(out_link)
    assert out_link == expected_link.replace(" ", "")


def test_aws_deepracer_evaluation_job_falls_back_to_service_home():
    arn = "arn:aws:deepracer:us-east-1:123456789012:evaluation_job/job123"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == "https://us-east-1.console.aws.amazon.com/deepracer/home?region=us-east-1"


def test_aws_service_only_arn_falls_back_to_service_home():
    arn = "arn:aws:ec2:ap-south-1:"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == "https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1"


def test_aws_logs_service_only_arn_uses_logs_home():
    arn = "arn:aws:logs:us-east-1:123456789012"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == "https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups"


def test_aws_arn_too_short_error():
    with pytest.raises(ARNTooShortError):
        aws.get_console_link(arn="arn:aws:ec2")


def test_aws_invalid_arn_error():
    with pytest.raises(InvalidARNError):
        aws.get_console_link(arn="bad:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0")


def test_aws_invalid_partition_error():
    with pytest.raises(InvalidPartitionError):
        aws.get_console_link(arn="arn:bad-partition:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0")


def test_aws_invalid_service_error():
    with pytest.raises(InvalidServiceError):
        aws.get_console_link(arn="arn:aws:not-a-service:us-east-1:123456789012:resource/id")


def test_aws_links_resource_keys_are_trimmed():
    links = get_links()

    for service, resource_types in links.items():
        for resource_type in resource_types:
            assert resource_type == resource_type.strip(), (
                f"{service!r} contains malformed resource key {resource_type!r}"
            )


def test_aws_get_service_home_link_returns_empty_when_service_missing():
    assert get_service_home_link({"service": "", "console": "console.aws.amazon.com"}) == ""


def test_aws_get_service_home_link_returns_empty_when_console_missing():
    assert get_service_home_link({"service": "ec2", "console": ""}) == ""


def test_aws_ec2_key_pair_slash_separator():
    # Standard ARN format: key-pair/name
    arn = "arn:aws:ec2:us-east-1:123456789012:key-pair/key-pair-name"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == "https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:"


def test_aws_ec2_key_pair_colon_separator():
    # Colon-separated format: key-pair:name
    arn = "arn:aws:ec2:us-east-1:123456789012:key-pair:key-pair-name"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == "https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:"


def test_aws_ec2_key_pair_trailing_colon_falls_back_to_key_pair_page():
    # ARN with trailing colon was the root cause: resource_tokens = ["key-pair/name", ""]
    # len > 1 branch was taken, setting resourceType = "key-pair/name" (slash included).
    # Fix ensures the slash-containing first token still goes through the path-split branch.
    arn = "arn:aws:ec2:us-east-1:123456789012:key-pair/key-pair-name:"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == "https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:"


def test_aws_network_firewall_firewall():
    arn = "arn:aws:network-firewall:us-east-1:123456789012:firewall/my-firewall"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == (
        "https://us-east-1.console.aws.amazon.com/vpc/home"
        "?region=us-east-1"
        "#FirewallDetails:firewallArn=arn:aws:network-firewall:us-east-1:123456789012:firewall/my-firewall"
    )


def test_aws_network_firewall_policy():
    arn = "arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/my-policy"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == (
        "https://us-east-1.console.aws.amazon.com/vpc/home"
        "?region=us-east-1"
        "#FirewallPolicyDetails:firewallPolicyArn=arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/my-policy"
    )


def test_aws_network_firewall_stateful_rulegroup():
    arn = "arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/my-rules"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == (
        "https://us-east-1.console.aws.amazon.com/vpc/home"
        "?region=us-east-1"
        "#StatefulRuleGroupDetails:ruleGroupArn=arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/my-rules"
    )


def test_aws_network_firewall_stateless_rulegroup():
    arn = "arn:aws:network-firewall:us-east-1:123456789012:stateless-rulegroup/my-rules"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == (
        "https://us-east-1.console.aws.amazon.com/vpc/home"
        "?region=us-east-1"
        "#StatelessRuleGroupDetails:ruleGroupArn=arn:aws:network-firewall:us-east-1:123456789012:stateless-rulegroup/my-rules"
    )


def test_aws_network_firewall_home():
    arn = "arn:aws:network-firewall:us-east-1:123456789012"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == "https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Firewalls:"


def test_aws_render_unknown_template_expression_returns_empty_string():
    result = _render("{unknown_expr}", {"region": "us-east-1", "console": "console.aws.amazon.com"})
    assert result == ""


def test_aws_network_firewall_unknown_resource_falls_back_to_home():
    arn = "arn:aws:network-firewall:us-east-1:123456789012:unknown-type/res-1"
    out_link = aws.get_console_link(arn=arn)
    assert out_link == "https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Firewalls:"


# ---------------------------------------------------------------------------
# Link gaps found auditing the ARNs cartography sends
# ---------------------------------------------------------------------------

AWS_LINK_CASES = {
    # Region-less ARNs drop the empty "{region}." host prefix and the bare region= parameter.
    "arn:aws:sso:::instance/ssoins-1": "https://console.aws.amazon.com/singlesignon/home",
    "arn:aws:sso:::permissionSet/ssoins-1/ps-2": "https://console.aws.amazon.com/singlesignon/home",
    "arn:aws:organizations::123456789012:organization/o-abc": "https://console.aws.amazon.com/organizations/v2/home",
    "arn:aws:lambda::123456789012:alias/fn": "https://console.aws.amazon.com/lambda/home#/functions/fn?tab=aliases",
    "arn:aws:dynamodb::123456789012:secondary_indexes/T": (
        "https://console.aws.amazon.com/dynamodbv2/home#table?initialTagKey=&name=T&tab=indexes"
    ),
    "arn:aws:dynamodb:eu-west-1:123456789012:secondary_indexes/T": (
        "https://eu-west-1.console.aws.amazon.com/dynamodbv2/home?region=eu-west-1"
        "#table?initialTagKey=&name=T&tab=indexes"
    ),
    # ECS: v2 console, cluster and id split out of the path.
    "arn:aws:ecs:us-east-1:123456789012:cluster/c1": (
        "https://us-east-1.console.aws.amazon.com/ecs/v2/clusters/c1?region=us-east-1"
    ),
    "arn:aws:ecs:us-east-1:123456789012:service/c1/svc": (
        "https://us-east-1.console.aws.amazon.com/ecs/v2/clusters/c1/services/svc?region=us-east-1"
    ),
    "arn:aws:ecs:us-east-1:123456789012:task/c1/0123abcd": (
        "https://us-east-1.console.aws.amazon.com/ecs/v2/clusters/c1/tasks/0123abcd?region=us-east-1"
    ),
    "arn:aws:ecs:us-east-1:123456789012:container-instance/c1/ci-1": (
        "https://us-east-1.console.aws.amazon.com/ecs/v2/clusters/c1/infrastructure?region=us-east-1"
    ),
    "arn:aws:ecs:us-east-1:123456789012:task-definition/family:3": (
        "https://us-east-1.console.aws.amazon.com/ecs/v2/task-definitions/family?region=us-east-1"
    ),
    "arn:aws:eks:us-east-1:123456789012:nodegroup/c1/ng1/uuid-1": (
        "https://us-east-1.console.aws.amazon.com/eks/home?region=us-east-1#/clusters/c1/nodegroups/ng1"
    ),
    "arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:uuid-1:autoScalingGroupName/my-asg": (
        "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#AutoScalingGroupDetails:id=my-asg"
    ),
    "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/x:*": (
        "https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1"
        "#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fx"
    ),
    "arn:aws:wafv2:us-east-2:123456789012:regional/webacl/acl1/id-1": (
        "https://us-east-2.console.aws.amazon.com/wafv2/homev2/web-acl/acl1/id-1/overview?region=us-east-2"
    ),
    "arn:aws:wafv2:us-east-1:123456789012:global/webacl/acl1/id-1": (
        "https://us-east-1.console.aws.amazon.com/wafv2/homev2/web-acl/acl1/id-1/overview?region=global"
    ),
    "arn:aws:config:us-east-1:123456789012:configuration-recorder/default": (
        "https://us-east-1.console.aws.amazon.com/config/home?region=us-east-1#/settings"
    ),
    "arn:aws:config:us-east-1:123456789012:delivery-channel/default": (
        "https://us-east-1.console.aws.amazon.com/config/home?region=us-east-1#/settings"
    ),
    "arn:aws:sns:us-east-1:123456789012:my-topic:0f1e2d3c": (
        "https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1"
        "#/subscription/arn:aws:sns:us-east-1:123456789012:my-topic:0f1e2d3c"
    ),
    "arn:aws:es:us-east-1:123456789012:reserved-instances/ri-1": (
        "https://us-east-1.console.aws.amazon.com/esv3/home?region=us-east-1#opensearch/reserved-instances"
    ),
    "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/lb1/50dc6c495c0c9188": (
        "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancer:loadBalancerArn="
        "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/lb1/50dc6c495c0c9188"
    ),
    "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/lb1/50dc6c495c0c9188": (
        "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancer:loadBalancerArn="
        "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/lb1/50dc6c495c0c9188"
    ),
    "arn:aws:elasticloadbalancing:us-east-1:123456789012:listener/app/lb1/50dc6c495c0c9188/f2f7dc8efc522ab2": (
        "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancer:loadBalancerArn="
        "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/lb1/50dc6c495c0c9188"
    ),
    # Classic load balancers keep the list page.
    "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/classic1": (
        "https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancers:sort=loadBalancerName"
    ),
    "arn:aws:route53:::hostedzone/Z123": "https://console.aws.amazon.com/route53/v2/hostedzones#ListRecordSets/Z123",
    "arn:aws:route53:::hostedzone//hostedzone/Z123": (
        "https://console.aws.amazon.com/route53/v2/hostedzones#ListRecordSets/Z123"
    ),
    "arn:aws:rds:us-east-1:123456789012:snapshot:rds:db1-2024-01-01": (
        "https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#db-snapshot:id=rds%3Adb1-2024-01-01"
    ),
    "arn:aws:rds:us-east-1:123456789012:subgrp:sg1": (
        "https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#db-subnet-group:id=sg1"
    ),
    "arn:aws:ec2:us-east-1:123456789012:transit-gateway-attachment/tgw-attach-1": (
        "https://us-east-1.console.aws.amazon.com/vpcconsole/home?region=us-east-1"
        "#TransitGatewayAttachmentDetails:transitGatewayAttachmentId=tgw-attach-1"
    ),
    "arn:aws:iam::123456789012:user/division/team/alice": "https://console.aws.amazon.com/iam/home?#/users/alice",
    "arn:aws:iam::123456789012:user/alice": "https://console.aws.amazon.com/iam/home?#/users/alice",
}


@pytest.mark.parametrize("arn,expected_link", AWS_LINK_CASES.items())
def test_aws_link_gap_fixes(arn, expected_link):
    assert aws.get_console_link(arn=arn) == expected_link


def test_aws_sns_topic_named_like_subscription_key_stays_a_topic():
    arn = "arn:aws:sns:us-east-1:123456789012:topic"
    assert aws.get_console_link(arn=arn).endswith("#/topic/arn:aws:sns:us-east-1:123456789012:topic")


def test_aws_wafv2_unsupported_kind_falls_back_to_home():
    arn = "arn:aws:wafv2:us-east-1:123456789012:regional/ipset/set1/id-1"
    assert aws.get_console_link(arn=arn) == "https://us-east-1.console.aws.amazon.com/wafv2/home?region=us-east-1"
