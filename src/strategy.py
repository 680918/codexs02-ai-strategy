
def calc_momentum(df):
    return df["close"].pct_change(5).iloc[-1]


def calc_volume(df):
    return df["vol"].rolling(5).mean().iloc[-1] / df["vol"].rolling(20).mean().iloc[-1]


def calc_rs(stock_ret, index_ret):
    return stock_ret - index_ret


def build_score(mom, vol, rs):
    score = (
        0.4 * mom +
        0.3 * vol +
        0.3 * rs
    )
    return score * 100