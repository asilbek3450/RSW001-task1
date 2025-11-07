import pytest
from storage.retry import retry

class Flaky:
    def __init__(self, fail_times=2):
        self.counter = 0
        self.fail_times = fail_times
    def op(self):
        self.counter += 1
        if self.counter <= self.fail_times:
            raise RuntimeError("fail")
        return "ok"

def test_retry_success():
    flaky = Flaky(fail_times=2)
    func = retry(max_attempts=5, delay=0)(flaky.op)
    assert func() == "ok"

def test_retry_fail():
    flaky = Flaky(fail_times=10)
    func = retry(max_attempts=3, delay=0)(flaky.op)
    with pytest.raises(RuntimeError):
        func()
