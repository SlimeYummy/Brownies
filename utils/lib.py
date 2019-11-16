
import time
import typing as T


def str_join(texts: T.List[str], sep: str = '') -> str:
    return sep.join(texts)


class APIProtector:
    def __init__(self, duration: float):
        self._last = 0
        self._duration = duration

    def protect(self):
        now = time.time()
        delta = now - self._last
        if delta < self._duration:
            time.sleep(self._duration - delta)
        self._last = time.time()
