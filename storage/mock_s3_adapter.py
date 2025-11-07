from typing import Dict
from .interface import FileStorage

class MockS3Adapter(FileStorage):
    def __init__(self):
        self.store: Dict[str, bytes] = {}

    def save_file(self, file_name: str, data: bytes) -> None:
        self.store[file_name] = data

    def read_file(self, file_name: str) -> bytes:
        if file_name not in self.store:
            raise FileNotFoundError(file_name)
        return self.store[file_name]

    def delete_file(self, file_name: str) -> None:
        if file_name in self.store:
            del self.store[file_name]
