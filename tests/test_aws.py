from cloudconsolelink.clouds.aws import AWS

aws = AWS()


def test_aws_instance():
    arn = "arn:aws:ec2:us-east1:1234567890:instance/instance1"
    expected_link = "https://us-east1.console.aws.amazon.com/ec2/v2/\
        home?region=us-east1#InstanceDetails:instanceId=instance1"

    out_link = aws.get_console_link(arn=arn)

    assert out_link == expected_link.replace(" ", "")
