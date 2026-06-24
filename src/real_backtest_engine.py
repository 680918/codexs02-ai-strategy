import pandas as pd
import numpy as np
from trade_cost import calc_trade_cost
from strategy import calc_momentum, calc_volume, calc_rs, build_score
from data_schema import validate_df


def get_common_dates(stock_data):
    """
    获取所有股票共同交易日期
    """
    date_sets = []

    for _, df in stock_data.items():
        if "trade_date" in df.columns:
            date_sets.append(set(df["trade_date"]))

    common_dates = set.intersection(*date_sets)

    return sorted(list(common_dates))


def get_price_on_date(df, trade_date):
    row = df[df["trade_date"] == trade_date]

    if row.empty:
        return None

    return float(row.iloc[0]["close"])


def get_window_df(df, trade_date, lookback=20):
    df = df.sort_values("trade_date").reset_index(drop=True)

    idx_list = df.index[df["trade_date"] == trade_date].tolist()

    if not idx_list:
        return None

    idx = idx_list[0]

    if idx < lookback:
        return None

    return df.iloc[idx - lookback: idx + 1]


def run_real_backtest(
    stock_data,
    index_data,
    weights,
    initial_capital=100000,
    top_n=2,
    rebalance_days=5,
    fee_rate=0.001
):
    """
    真实持仓回测：
    - 每 rebalance_days 天调仓一次
    - 每次选 score 最高的 top_n 股票
    - 等权买入
    - 每日计算净值
    """

    cash = initial_capital
    positions = {}
    equity_curve = []

    dates = get_common_dates(stock_data)

    if len(dates) == 0:
        raise ValueError("没有共同交易日期，无法回测")

    index_data = index_data.sort_values("trade_date").reset_index(drop=True)

    for i, trade_date in enumerate(dates):

        # 计算每日净值
        stock_value = 0

        for code, qty in positions.items():
            price = get_price_on_date(stock_data[code], trade_date)
            if price is not None:
                stock_value += qty * price

        total_value = cash + stock_value
        equity_curve.append((trade_date, total_value))

        # 到调仓日才调仓
        if i % rebalance_days != 0:
            continue

        scores = {}

        index_window = get_window_df(index_data, trade_date, lookback=20)

        if index_window is None:
            continue

        index_ret = index_window["close"].pct_change().iloc[-1]

        for code, df in stock_data.items():

            df = validate_df(df)

            window_df = get_window_df(df, trade_date, lookback=20)

            if window_df is None or window_df.empty:
                continue

            try:
                mom = calc_momentum(window_df)
                vol = calc_volume(window_df)
                rs = calc_rs(window_df["close"].pct_change().iloc[-1], index_ret)

                if np.isnan(mom) or np.isnan(vol) or np.isnan(rs):
                    continue

                score = build_score(mom, vol, rs)

                scores[code] = score

            except Exception:
                continue

        if len(scores) == 0:
            continue

        selected = sorted(scores, key=scores.get, reverse=True)[:top_n]

        # 先卖出旧持仓
        for code, qty in list(positions.items()):
            price = get_price_on_date(stock_data[code], trade_date)
            if price is None:
                continue

            amount = qty * price
            cost = calc_trade_cost(amount, fee_rate)
            cash += amount - cost

        positions = {}

        # 再买入新组合
        available_cash = cash
        each_amount = available_cash / len(selected)

        for code in selected:
            price = get_price_on_date(stock_data[code], trade_date)
            if price is None or price <= 0:
                continue

            cost = calc_trade_cost(each_amount, fee_rate)
            buy_amount = each_amount - cost
            qty = buy_amount / price

            positions[code] = qty
            cash -= each_amount

    return equity_curve