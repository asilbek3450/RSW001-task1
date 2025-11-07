from abc import ABC, abstractmethod

class FileStorage(ABC):
    @abstractmethod
    def save_file(self, file_name: str, data: bytes) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_file(self, file_name: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, file_name: str) -> None:
        raise NotImplementedError
