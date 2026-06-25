from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from safe_engine import validate_portfolio
from market_data import get_price
from execution_v2 import execute_trade


def run_v58(stock_data, index_data, scores):

    equity_curve = []
    capital = 100000

    for day in range(10):

        print(f"\n📅 Day {day+1}")

        # ① 信号
        selected = build_signal_portfolio(stock_data)

        # ② 组合
        raw_portfolio = allocate_portfolio(selected, scores, capital)

        # ③ 安全校验
        portfolio = validate_portfolio(raw_portfolio)

        new_capital = capital

        # ④ 🚀 真实撮合执行
        for code, amount in portfolio.items():

            price = get_price(code, day)

            exec_price = execute_trade(price, amount)

            new_capital -= amount  # 已成交资金

        # ⑤ T+1约束（简化）
        capital = new_capital

        equity_curve.append(capital)

    return equity_curve