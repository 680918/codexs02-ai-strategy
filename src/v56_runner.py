from paper_trader import PaperAccount
from rebalance_engine import rebalance


def run_v56(stock_data, index_data, scores, days=10):

    account = PaperAccount()

    def step(day):

        print("🔁 调仓日:", day)

        portfolio = rebalance(stock_data, scores, account.cash)

        prices = {k: 100 for k in stock_data.keys()}  # 简化价格

        value = account.update(portfolio, prices)

        print("💰 账户净值:", value)

        return value

    history = []

    for d in range(days):
        history.append(step(d))

    return history