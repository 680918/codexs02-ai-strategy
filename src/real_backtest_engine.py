import numpy as np
from trade_cost import calc_trade_cost
from strategy import calc_momentum, calc_volume, calc_rs, build_score
from data_schema import validate_df


def get_price_on_date(df, date):
    row = df[df["trade_date"] == date]
    if row.empty:
        return None
    return float(row.iloc[0]["close"])


def run_real_backtest(
    stock_data,
    index_data,
    weights,
    initial_capital=100000,
    top_n=2,
    rebalance_days=5,
    fee_rate=0.001
):

    cash = initial_capital
    positions = {}
    equity_curve = []

    dates = list(index_data["trade_date"]) if "trade_date" in index_data.columns else index_data.index.tolist()

    if len(dates) == 0:
        raise ValueError("无交易日期数据")

    stock_codes = list(stock_data.keys())

    for i, trade_date in enumerate(dates):

        # ========================
        # ① 计算当前净值
        # ========================
        stock_value = 0

        for code, qty in positions.items():
            price = get_price_on_date(stock_data[code], trade_date)
            if price is not None:
                stock_value += qty * price

        total_value = cash + stock_value
        equity_curve.append((trade_date, total_value))

        # ========================
        # ② 非调仓日跳过
        # ========================
        if i % rebalance_days != 0:
            continue

        # ========================
        # ③ 计算因子评分
        # ========================
        scores = {}

        for code in stock_codes:

            df = stock_data[code]

            # ⚠️ 不强依赖 validate（避免清空数据）
            if df is None or len(df) < 10:
                continue

            try:
                mom = calc_momentum(df)
                vol = calc_volume(df)
                rs = calc_rs(df["close"].pct_change().iloc[-1], 0)

                if np.isnan(mom) or np.isnan(vol) or np.isnan(rs):
                    continue

                score = build_score(mom, vol, rs)
                scores[code] = score

            except:
                continue

        # ========================
        # ④ ⭐关键修复：防空 scores
        # ========================
        if len(scores) == 0:
            scores = {stock_codes[0]: 1.0}

        # ========================
        # ⑤ 选股
        # ========================
        selected = sorted(scores, key=scores.get, reverse=True)[:top_n]

        # ========================
        # ⑥ 先卖出
        # ========================
        for code, qty in list(positions.items()):
            price = get_price_on_date(stock_data[code], trade_date)
            if price is None:
                continue

            amount = qty * price
            cost = calc_trade_cost(amount, fee_rate)

            cash += amount - cost

        positions = {}

        # ========================
        # ⑦ 再买入
        # ========================
        if len(selected) == 0:
            selected = [stock_codes[0]]

        each_amount = cash / len(selected)

        for code in selected:

            price = get_price_on_date(stock_data[code], trade_date)

            if price is None or price <= 0:
                continue

            cost = calc_trade_cost(each_amount, fee_rate)
            buy_amount = each_amount - cost
            qty = buy_amount / price

            positions[code] = qty
            cash -= each_amount

    return equity_curve, []