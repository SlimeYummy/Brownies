import datetime as D
import common as C
import utils as U


FIRST_TRADING_DATE = D.date(year=2010, month=1, day=1)
FIRST_TRADING_TIME = FIRST_TRADING_DATE.strftime('%Y%m%d')


def _compute_last_trading_date() -> D.date:
    now = D.datetime.today()
    end_date = D.date.today()
    if now.hour < 17:  # tushare update data before 17:00
        end_date = end_date - D.timedelta(1)

    data_frame = C.tuapi.trade_cal(
        exchange='SSE',
        start_date=U.date_to_str(end_date - D.timedelta(90)),
        end_date=U.date_to_str(end_date)
    )
    for _, row in data_frame.iloc[::-1].iterrows():
        if row['is_open']:
            return U.str_to_date(row['cal_date'])
    return None


LAST_TRADING_DATE: D.date = _compute_last_trading_date()
LAST_TRADING_TIME = LAST_TRADING_DATE.strftime('%Y%m%d')
