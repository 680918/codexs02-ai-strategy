
from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from v56_runner import run_v56


def run_v57(stock_data, index_data, scores):

    equity_curve = []
    capital = 100000

    for day in range(10):

        print(f"\n📅 Day {day+1}")

        # ✔ 正确：重新生成信号组合
        selected = build_signal_portfolio(stock_data)

        portfolio = allocate_portfolio(selected, scores, capital)

        # ✔ 保证类型正确
        if not isinstance(portfolio, dict):
            portfolio = {}

        new_capital = capital

        for code, amount in portfolio.items():

            price = 100  # mock price

            new_capital -= amount * 0.001

        equity_curve.append(new_capital)

        capital = new_capital

    return equity_curve