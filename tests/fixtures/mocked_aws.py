import os

import boto3
from moto import mock_aws
from pytest import fixture

from tests.consts import TEST_BUCKET_NAME


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
        response = s3_client.list_objects_v2(Bucket=TEST_BUCKET_NAME)
        for obj in response.get("Contents", []):
            s3_client.delete_object(Bucket=TEST_BUCKET_NAME, Key=obj["Key"])
        s3_client.delete_bucket(Bucket=TEST_BUCKET_NAME)
