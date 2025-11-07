import os
from storage.local_adapter import LocalStorageAdapter

def test_local_save_read_delete(tmp_path):
    adapter = LocalStorageAdapter(str(tmp_path))
    adapter.save_file("dir1/test.bin", b"hello")
    assert (tmp_path/"dir1/test.bin").exists()
    data = adapter.read_file("dir1/test.bin")
    assert data == b"hello"
    adapter.delete_file("dir1/test.bin")
    assert not (tmp_path/"dir1/test.bin").exists()
