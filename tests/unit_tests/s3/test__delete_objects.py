"""Testing the delete_objects module."""

import boto3
from moto import mock_aws

from files_api.s3.delete_objects import delete_s3_object
from files_api.s3.read_objects import object_exists_in_s3
from files_api.s3.write_objects import upload_s3_object
from tests.consts import (
    TEST_BUCKET_NAME,
    TEST_OBJECT_KEY,
)
from tests.unit_tests.s3.test__write_objects import test__upload_s3_object


# pylint: disable=unused-argument
def test_delete_existing_s3_object(mocked_aws: None):
    s3_client = boto3.client("s3")
    s3_client.put_object(Bucket=TEST_BUCKET_NAME, Key="testfile.txt", Body="test content")
    delete_s3_object(TEST_BUCKET_NAME, "testfile.txt")
    assert not s3_client.list_objects_v2(Bucket=TEST_BUCKET_NAME).get("Contents")
