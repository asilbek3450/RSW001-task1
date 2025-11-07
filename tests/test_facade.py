from storage.facade import StorageFacade

def test_facade_local(tmp_path):
    config = {'mode': 'local', 'local_path': str(tmp_path)}
    f = StorageFacade(config)
    f.save_file("t.txt", b"1")
    assert f.read_file("t.txt") == b"1"
    f.delete_file("t.txt")

def test_facade_mock_s3():
    config = {'mode': 'mock_s3'}
    f = StorageFacade(config)
    f.save_file("t.txt", b"2")
    assert f.read_file("t.txt") == b"2"
    f.delete_file("t.txt")