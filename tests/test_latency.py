import time
from storage.mock_s3_adapter import MockS3Adapter
import statistics

def measure(adapter, runs=100):
    times = []
    for i in range(runs):
        start = time.perf_counter()
        adapter.save_file(f"file_{i}.bin", b"x"*1024)
        end = time.perf_counter()
        times.append(end-start)
    return times

def test_latency_stats():
    adapter = MockS3Adapter()
    times = measure(adapter, runs=50)
    avg = statistics.mean(times)
    med = statistics.median(times)
    mx = max(times)
    mn = min(times)
    stdev = statistics.stdev(times) if len(times) > 1 else 0.0
    assert avg >= 0.0
    print("latency avg", avg, "median", med, "min", mn, "max", mx, "stdev", stdev)
