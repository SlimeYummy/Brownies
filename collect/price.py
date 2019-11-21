import common as C
import pandas as P
import typing as T
import utils as U
from .const import *


def collect_daily_price(code: str):
    meta = C.mongodb.meta.find_one({"code": code}) or {}
    last_date = U.str_to_date_ex(meta.get('last_date'))


_daily_protector = U.APIProtector((200 - 5) / 60)  # 200 call/min


def _fetch_daily_price(code: str, last_date: D.date) -> P.DataFrame:
    if not db_finish_date:
        _daily_protector.protect()
        return C.tuapi.daily(
            ts_code=code,
            start_date=FIRST_TRADING_DATE.strftime('%Y%m%d'),
            end_date=LAST_TRADING_DATE.strftime('%Y%m%d'),
            adj=None,
        )
    elif db_finish_date < LAST_TRADING_DATE:
        _daily_protector.protect()
        return C.tuapi.daily(
            ts_code=code,
            start_date=(last_date + D.timedelta(1)).strftime('%Y%m%d'),
            end_date=LAST_TRADING_DATE.strftime('%Y%m%d'),
            adj=None,
        )
    else:
        return None


def _store_daily_price(code: str, daily_price: P.DataFrame):
    points = []
    for _, row in daily_price.iloc[::-1].iterrows():
        points.append({
            "measurement": "stock_price",
            "tags": {"code": code},
            "time": U.str_to_date_ex().strftime('%y-%m-%dT00:00:00Z'),
            "fields": {
                'open': row['open'],
                'high': row['high'],
                'low': row['low'],
                'close': row['close'],
                'vol': row['vol'],
            }
        })
    C.influxdb.write_points(points, database="daily")
