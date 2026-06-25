import tushare as ts
import pandas as pd

pro = ts.pro_api("98cf930ca6e181e63f7e2a06e000d3bffc0e2fbda56b2fd6435da46b")


def get_stock_data(ts_code):
    df = pro.daily(ts_code=ts_code, fields="ts_code,trade_date,close,vol,open,high,low")

    df = df.sort_values("trade_date")
    return df


def get_moneyflow(ts_code):
    """
    真实主力资金流
    """
    df = pro.moneyflow(ts_code=ts_code)

    return df