import logging

from clouds.aws import get_aws_console_link

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(cloud: str, id: str) -> str:
    clouds = {
        "aws": get_aws_console_link,
    }
    if cloud in clouds:
        return clouds[cloud](id)
    else:
        raise ValueError(f"Cloud '{cloud}' does not exist. Did you misspell it?")


if __name__ == '__main__':
    arn: str = "arn:aws:ec2:us-east-2:58134515:instance/i-78ddb476422"
    response = main('aws', arn)
    logger.info("%s", response)
