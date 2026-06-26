from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from execution_v2 import execute_trade
from market_data import get_price


def run_runtime(stock_data, index_data, scores, day):

    print(f"\n📊 v5.9 runtime Day {day}")

    capital = 100000

    selected = build_signal_portfolio(stock_data)

    portfolio = allocate_portfolio(selected, scores, capital)

    new_capital = capital

    for code, amount in portfolio.items():

        price = get_price(code, day)

        exec_price = execute_trade(price, amount)

        new_capital -= amount

    print("💰 净值:", new_capital)

    return new_capital