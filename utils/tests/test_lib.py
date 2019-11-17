import time
from ..lib import *


def test_str_join():
    res = str_join(["a", "b"])
    assert res == "ab"


def test_api_protector_defer():
    protector = APIProtector(0.1)

    t1 = time.time()
    protector.protect()
    t2 = time.time()
    assert t2 - t1 < 0.01

    t3 = time.time()
    protector.protect()
    t4 = time.time()
    assert t4 - t3 >= 0.1

    time.sleep(0.15)
    t5 = time.time()
    protector.protect()
    t6 = time.time()
    assert t6 - t5 < 0.01
