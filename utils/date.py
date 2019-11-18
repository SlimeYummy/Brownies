import datetime as D
import typing as T


def str_to_date(text: str) -> D.date:
    if not text:
        return None
    try:
        return D.datetime.strptime(text, '%Y%m%d').date()
    except:
        return None


def str_to_date_ex(text: str) -> D.date:
    if not text:
        return None
    return D.datetime.strptime(text, '%Y%m%d').date()


def date_to_str(day: D.date) -> str:
    if not day:
        return ''
    try:
        return day.strftime('%Y%m%d')
    except:
        return ''


def date_to_str_ex(day: D.date) -> str:
    if not day:
        return ''
    return day.strftime('%Y%m%d')


def date_delta(a: T.Any, b: T.Any) -> D.timedelta:
    x = a if type(a) != str else str_to_date_ex(a)
    y = b if type(b) != str else str_to_date_ex(b)
    return x - y


def date_min(a: T.Any, b: T.Any) -> T.Any:
    x = a if type(a) != str else str_to_date_ex(a)
    y = b if type(b) != str else str_to_date_ex(b)
    if x <= y:
        return a
    else:
        return b


def date_max(a: T.Any, b: T.Any) -> T.Any:
    x = a if type(a) != str else str_to_date_ex(a)
    y = b if type(b) != str else str_to_date_ex(b)
    if x >= y:
        return a
    else:
        return b


def date_less(a: T.Any, b: T.Any) -> bool:
    x = a if type(a) != str else str_to_date_ex(a)
    y = b if type(b) != str else str_to_date_ex(b)
    return x < y


def date_greater(a: T.Any, b: T.Any) -> bool:
    x = a if type(a) != str else str_to_date_ex(a)
    y = b if type(b) != str else str_to_date_ex(b)
    return x > y
