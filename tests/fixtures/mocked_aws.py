import os

import boto3
import botocore
from moto import mock_aws
from pytest import fixture

from tests.consts import TEST_BUCKET_NAME
from tests.utils import delete_s3_bucket


def point_away_aws():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-west-2"


@fixture
def mocked_aws():
    with mock_aws():
        point_away_aws()

        # Create a S3 bucket
        s3_client = boto3.client(
            "s3",
            region_name="us-west-2",
        )
        s3_client.create_bucket(
            Bucket=TEST_BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": "us-west-2"},
        )

        yield

        # Clean up the bucket
        try:
            delete_s3_bucket(TEST_BUCKET_NAME)
        except botocore.exceptions.ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchBucket":
                pass
            else:
                raise
