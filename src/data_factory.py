import numpy as np
import pandas as pd

from data_guard import safe_df


def create_stock_data():

    def fake():

        return pd.DataFrame({
            "close": np.random.rand(30) * 100 + 50,
            "vol": np.random.rand(30) * 1000 + 100
        })

    raw_data = {
        "000001.SZ": fake(),
        "300750.SZ": fake(),
        "600519.SH": fake()
    }

    # 🛡 全部过防火墙
    clean_data = {}

    for k, v in raw_data.items():
        clean_data[k] = safe_df(v)

    return clean_data