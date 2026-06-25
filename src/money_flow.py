import pandas as pd
import numpy as np

def calculate_money_flow(stock_data):
    """
    简化资金流模型：
    用成交量 + 涨跌幅 proxy 主力行为
    """

    results = []

    for code, df in stock_data.items():

        if len(df) < 20:
            continue

        try:
            ret = df["close"].pct_change(5).iloc[-1]
            vol = df["vol"].pct_change(5).iloc[-1]

            # 简化资金流评分
            mf_score = ret * 0.6 + vol * 0.4

            results.append({
                "code": code,
                "return_5d": ret,
                "volume_change": vol,
                "money_flow_score": mf_score
            })

        except:
            continue

    return pd.DataFrame(results).sort_values("money_flow_score", ascending=False)


def get_top_money_flow(stock_data, top_n=5):
    df = calculate_money_flow(stock_data)
    return df.head(top_n)