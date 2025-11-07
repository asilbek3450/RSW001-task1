from .local_adapter import LocalStorageAdapter
from .s3_adapter import S3StorageAdapter
from .mock_s3_adapter import MockS3Adapter
from .interface import FileStorage

class StorageFacade:
    def __init__(self, config: dict):
        mode = config.get('mode', 'local')
        if mode == 'local':
            path = config.get('local_path', './data')
            self.backend: FileStorage = LocalStorageAdapter(path)
        elif mode == 's3':
            bucket = config['s3_bucket']
            region = config.get('s3_region')
            endpoint = config.get('s3_endpoint')
            self.backend = S3StorageAdapter(bucket_name=bucket, region_name=region, endpoint_url=endpoint)
        elif mode == 'mock_s3':
            self.backend = MockS3Adapter()
        else:
            raise ValueError('unknown storage mode')

    def save_file(self, file_name: str, data: bytes) -> None:
        return self.backend.save_file(file_name, data)

    def read_file(self, file_name: str) -> bytes:
        return self.backend.read_file(file_name)

    def delete_file(self, file_name: str) -> None:
        return self.backend.delete_file(file_name)
