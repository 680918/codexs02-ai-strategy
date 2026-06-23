
from tushare_client import get_stock, get_index

STOCKS = ["600519.SH", "000001.SZ", "601318.SH"]

def load_real_data():
    stock_data = {}

    for s in STOCKS:
        stock_data[s] = get_stock(s, "20240101", "20240301")

    index_data = get_index("20240101", "20240301")

    return stock_data, index_data