from cloudconsolelink.clouds.aws import AWSLinker

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
