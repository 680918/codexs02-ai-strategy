from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from safe_engine import validate_portfolio


def run_v57_stable(stock_data, index_data, scores):

    equity_curve = []
    capital = 100000

    for day in range(10):

        print(f"\n📅 Day {day+1}")

        # ① 信号
        selected = build_signal_portfolio(stock_data)

        # ② 组合
        raw_portfolio = allocate_portfolio(selected, scores, capital)

        # ③ 🛡 安全校验（关键）
        portfolio = validate_portfolio(raw_portfolio)

        new_capital = capital

        # ④ 执行
        for code, amount in portfolio.items():

            price = 100  # mock price

            new_capital -= amount * 0.001

        equity_curve.append(new_capital)

        capital = new_capital

    return equity_curve