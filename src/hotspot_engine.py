import pandas as pd
import numpy as np

def detect_hotspots(stock_data):
    """
    简化版热点识别：
    用涨幅 + 动量 + 成交量变化
    """

    results = []

    for code, df in stock_data.items():

        if len(df) < 20:
            continue

        try:
            ret = df["close"].pct_change(5).iloc[-1]
            vol = df["vol"].pct_change(5).iloc[-1]
            mom = df["close"].pct_change(10).iloc[-1]

            score = ret * 0.5 + vol * 0.3 + mom * 0.2

            results.append({
                "code": code,
                "return_5d": ret,
                "volume_change": vol,
                "momentum": mom,
                "score": score
            })

        except:
            continue

    df_res = pd.DataFrame(results)
    df_res = df_res.sort_values("score", ascending=False)

    return df_res


def get_top_hotspots(stock_data, top_n=5):
    df = detect_hotspots(stock_data)
    return df.head(top_n)