import pytest
from storage.mock_s3_adapter import MockS3Adapter

def test_mock_s3_basic():
    adapter = MockS3Adapter()
    adapter.save_file("a.txt", b"x")
    assert adapter.read_file("a.txt") == b"x"
    adapter.delete_file("a.txt")
    with pytest.raises(FileNotFoundError):
        adapter.read_file("a.txt")
