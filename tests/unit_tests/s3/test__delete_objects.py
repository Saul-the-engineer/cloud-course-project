"""Testing the delete_objects module."""

import boto3
from moto import mock_aws

from files_api.s3.delete_objects import delete_s3_object
from tests.consts import (
    TEST_BUCKET_NAME,
    TEST_OBJECT_KEY,
)
from tests.unit_tests.s3.test__write_objects import test__upload_s3_object


@mock_aws
def test__delete_s3_object(mocked_aws: None) -> None:
    # upload a file to the bucket
    test__upload_s3_object(mocked_aws)

    # delete the file
    delete_s3_object(bucket_name=TEST_BUCKET_NAME, object_key=TEST_OBJECT_KEY)

    # Check that the file was deleted
    try:
        s3_client = boto3.client("s3")
        s3_client.get_object(Bucket=TEST_BUCKET_NAME, Key=TEST_OBJECT_KEY)
        assert False, "The file was not deleted"
    except s3_client.exceptions.NoSuchKey:
        pass
