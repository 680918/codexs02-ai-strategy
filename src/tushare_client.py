import tushare as ts
import pandas as pd

ts.set_token("98cf930ca6e181e63f7e2a06e000d3bffc0e2fbda56b2fd6435da46b")
pro = ts.pro_api()

def get_stock(ts_code, start, end):
    df = pro.daily(ts_code=ts_code, start_date=start, end_date=end)
    df = df.sort_values("trade_date")
    df["ret"] = df["close"].pct_change()
    return df


def get_index(start, end):
    df = pro.index_daily(ts_code="000300.SH", start_date=start, end_date=end)
    df = df.sort_values("trade_date")
    df["ret"] = df["close"].pct_change()
    return df