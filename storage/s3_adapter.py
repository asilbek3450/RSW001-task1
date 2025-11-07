import boto3
from botocore.exceptions import BotoCoreError, ClientError
from .interface import FileStorage

class S3StorageAdapter(FileStorage):
    def __init__(self, bucket_name: str, region_name: str = None, endpoint_url: str = None):
        session = boto3.session.Session()
        self.client = session.client('s3', region_name=region_name, endpoint_url=endpoint_url)
        self.bucket = bucket_name

    def save_file(self, file_name: str, data: bytes) -> None:
        try:
            self.client.put_object(Bucket=self.bucket, Key=file_name, Body=data)
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(str(e))

    def read_file(self, file_name: str) -> bytes:
        try:
            resp = self.client.get_object(Bucket=self.bucket, Key=file_name)
            return resp['Body'].read()
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(str(e))

    def delete_file(self, file_name: str) -> None:
        try:
            self.client.delete_object(Bucket=self.bucket, Key=file_name)
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(str(e))
