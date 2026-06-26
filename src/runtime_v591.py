from account_state import AccountState
from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from safe_engine import validate_portfolio
from pnl_engine import calc_portfolio_value
from market_simulator import get_price


def run_v591(stock_data, index_data, scores):

    account = AccountState()

    history = []

    for day in range(5):

        print(f"\n📅 Day {day}")

        selected = build_signal_portfolio(stock_data)

        raw_portfolio = allocate_portfolio(selected, scores, 100000)

        portfolio = validate_portfolio(raw_portfolio)

        account.update_position(portfolio)

        value = calc_portfolio_value(account)

        account.record(value)

        history.append(value)

        print("💰 净值:", value)

    return history


if __name__ == "__main__":

    from data_factory import create_stock_data

    stock_data = create_stock_data()

    index_data = None

    scores = {
        "000001.SZ": 20,
        "300750.SZ": 35,
        "600519.SH": 25
    }

    result = run_v591(stock_data, index_data, scores)

    print("\n===== v5.9.1结果 =====")
    print(result)