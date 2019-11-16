import pytest
import datetime as D
from ..date import *


def test_str_to_date():
    assert str_to_date_ex('20190101') == D.date(2019, 1, 1)
    assert str_to_date('20190101') == D.date(2019, 1, 1)


def test_date_to_str():
    assert date_to_str(D.date(2019, 1, 1)) == '20190101'
    assert date_to_str_ex(D.datetime(2019, 1, 1)) == '20190101'


def test_date_delta():
    assert date_delta('20190120', D.date(2019, 1, 1)) == D.timedelta(19)


def test_date_min():
    assert date_min('20190120', D.date(2019, 1, 1)) == D.date(2019, 1, 1)


def test_date_max():
    assert date_max('20190120', D.date(2019, 1, 1)) == '20190120'


def test_date_less():
    assert date_less('20190120', D.date(2019, 1, 1)) == False


def test_date_greater():
    assert date_greater('20190120', D.date(2019, 1, 1)) == True
