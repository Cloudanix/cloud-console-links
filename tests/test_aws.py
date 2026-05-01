from cloudconsolelink.clouds.aws import AWSLinker
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
    expected_link = "https://us-east1.console.aws.amazon.com/ecr/repositories/repo1\
        ?region=us-east1"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


def test_aws_eks_cluster():
    arn = "arn:aws:eks:us-east-2:1234567890:cluster/testing-cluster"
    expected_link = "https://us-east-2.console.aws.amazon.com/eks/home?region=\
        us-east-2#/clusters/testing-cluster"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")


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


def test_aws_cloudwatch_loggroup():
    arn = "arn:aws:logs:us-east-2:123456789012:log-group/LogGroupName-123"
    expected_link = 'https://https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#logsV2:log-groups/log-group/LogGroupName-123'

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

    assert out_link == "https://console.aws.amazon.com/deepracer"


def test_aws_links_resource_keys_are_trimmed():
    links = get_links()

    for service, resource_types in links.items():
        for resource_type in resource_types:
            assert resource_type == resource_type.strip(), (
                f"{service!r} contains malformed resource key {resource_type!r}"
            )
