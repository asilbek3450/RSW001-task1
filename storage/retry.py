import time
from typing import Callable

def retry(max_attempts: int = 3, delay: float = 0.1, allowed_exceptions: tuple = (Exception,)):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as e:
                    last = e
                    time.sleep(delay)
            raise last
        return wrapper
    return deco
