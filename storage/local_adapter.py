from pathlib import Path
from .interface import FileStorage

class LocalStorageAdapter(FileStorage):
    def __init__(self, base_path: str):
        self.base = Path(base_path)
        self.base.mkdir(parents=True, exist_ok=True)

    def _path(self, file_name: str) -> Path:
        return self.base / file_name

    def save_file(self, file_name: str, data: bytes) -> None:
        p = self._path(file_name)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    def read_file(self, file_name: str) -> bytes:
        p = self._path(file_name)
        return p.read_bytes()

    def delete_file(self, file_name: str) -> None:
        p = self._path(file_name)
        if p.exists():
            p.unlink()
