def run_backtest(stock_data, index_data, weights):

    index_ret = index_data["close"].pct_change().iloc[-1]

    total = 100000

    for code, df in stock_data.items():

        mom = df["close"].pct_change(5).iloc[-1]
        vol = df["vol"].rolling(5).mean().iloc[-1]
        rs = df["close"].pct_change().iloc[-1] - index_ret

        score = (
            weights["momentum"] * mom +
            weights["volume"] * vol +
            weights["rs"] * rs
        )

        total += score * 1000

    return total