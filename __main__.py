from clouds.aws import process_arn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    arn: str = "arn:aws:ec2:us-east-2:58134515:instance/i-78ddb476422"
    response = process_arn(arn)
    logger.info("%s", response)
