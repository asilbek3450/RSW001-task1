from storage.facade import StorageFacade

def demo_local():
    cfg = {'mode':'local','local_path':'./demo_data'}
    s = StorageFacade(cfg)
    s.save_file('hello.txt', b'hello world')
    print(s.read_file('hello.txt'))
    s.delete_file('hello.txt')

def demo_mock_s3():
    cfg = {'mode':'mock_s3'}
    s = StorageFacade(cfg)
    s.save_file('a.txt', b'abc')
    print(s.read_file('a.txt'))
    s.delete_file('a.txt')

if __name__ == "__main__":
    demo_local()
    demo_mock_s3()
