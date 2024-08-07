"""This script writes a file to an S3 bucket. """

import boto3

try:
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.type_defs import (
        PutObjectOutputTypeDef,
        ResponseMetadataTypeDef,
    )
except ImportError:
    print("boto3-stubs not installed. Please run `pip install boto3-stubs`")

BUCKET_NAME = "cloud-course-bucket-saul"

session = boto3.Session(profile_name="cloud-course")
s3_client: "S3Client" = session.client("s3")

# s3_client = boto3.client("s3")
# write a file to S3 bucket with the contents "Hello, World!"
response: "PutObjectOutputTypeDef" = s3_client.put_object(
    Bucket=BUCKET_NAME,
    Key="folder/hello.txt",
    Body="Hello, World!",
    ContentType="text/plain",
)
