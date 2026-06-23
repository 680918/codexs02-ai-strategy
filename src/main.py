from data import load_real_data
from strategy import calc_momentum, calc_volume, calc_rs, build_score


def run():
    stock_data, index_data = load_real_data()

    index_ret = index_data["close"].pct_change().iloc[-1]

    results = {}

    for code, df in stock_data.items():

        mom = calc_momentum(df)
        vol = calc_volume(df)
        rs = calc_rs(df["close"].pct_change().iloc[-1], index_ret)

        score = build_score(mom, vol, rs)

        results[code] = score

        print(code, "score:", round(score, 2))

    best = max(results, key=results.get)

    print("\n===== v4.2结果 =====")
    print("最强股票:", best)
    print("评分:", results[best])


if __name__ == "__main__":
    run()