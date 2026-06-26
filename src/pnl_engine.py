from market_simulator import get_price

def calc_portfolio_value(account):

    total = account.cash

    for code, amount in account.positions.items():

        price = get_price(code, 0)

        total += amount * price

    return total

