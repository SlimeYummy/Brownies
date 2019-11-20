import tushare
from . import config

tushare.set_token(config.TU_SHARE_TOKEN)
tuapi = tushare.pro_api()
