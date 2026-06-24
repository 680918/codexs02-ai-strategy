import numpy as np

def run_backtest(stock_data, index_data, weights):

    total = 100000

    index_ret = index_data["close"].pct_change().fillna(0).iloc[-1]

    for code, df in stock_data.items():

        mom = df["close"].pct_change(5).fillna(0).iloc[-1]
        vol = df["vol"].rolling(5).mean().fillna(0).iloc[-1]
        rs = df["close"].pct_change().fillna(0).iloc[-1] - index_ret

        score = (
            weights["momentum"] * mom +
            weights["volume"] * vol +
            weights["rs"] * rs
        )

        # 🟢 关键：让收益变化
        total += score * 1000

    return total