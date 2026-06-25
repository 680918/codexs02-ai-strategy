from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio


def rebalance(stock_data, scores, capital):

    selected = build_signal_portfolio(stock_data)

    portfolio = allocate_portfolio(selected, scores, capital)

    return portfolio