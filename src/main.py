from portfolio import build_portfolio
from risk import risk_adjust
from data import load_real_data
from strategy import calc_momentum, calc_volume, calc_rs, build_score
from data_schema import validate_df
from logger import Logger
from report import generate_report


def run():

    logger = Logger()

    stock_data, index_data = load_real_data()

    index_ret = index_data["close"].pct_change().iloc[-1]

    scores = {}

    for code, df in stock_data.items():

          # 🟢 ★ 这里是你要加的地方（第一步）
        df = validate_df(df)

        # 🟢 ★ 防止空数据（第二步）
        if df.empty:
            continue

        mom = calc_momentum(df)
        vol = calc_volume(df)
        rs = calc_rs(df["close"].pct_change().iloc[-1], index_ret)

        score = build_score(mom, vol, rs)

        scores[code] = score

        
    portfolio = build_portfolio(scores)

    
    print("\n===== v4.3组合系统 =====")

    for code in portfolio:

        adj = risk_adjust(portfolio[code], scores[code])

        logger.log(f"{code} score: {round(scores[code],2)} allocation: {round(adj,2)}")

    generate_report(None, logger.get_logs())


if __name__ == "__main__":
    run()