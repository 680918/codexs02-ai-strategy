from portfolio import build_portfolio
from risk import risk_adjust
from data import load_real_data
from strategy import calc_momentum, calc_volume, calc_rs, build_score


def run():

    stock_data, index_data = load_real_data()

    index_ret = index_data["close"].pct_change().iloc[-1]

    scores = {}

    for code, df in stock_data.items():

        mom = calc_momentum(df)
        vol = calc_volume(df)
        rs = calc_rs(df["close"].pct_change().iloc[-1], index_ret)

        score = build_score(mom, vol, rs)

        scores[code] = score

    portfolio = build_portfolio(scores)

    print("\n===== v4.3组合系统 =====")

    for k in portfolio:

        adj = risk_adjust(portfolio[k], scores[k])

        print(k, "score:", round(scores[k], 2), "allocation:", round(adj, 2))


if __name__ == "__main__":
    run()