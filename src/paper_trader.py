class PaperAccount:

    def __init__(self, capital=100000):
        self.cash = capital
        self.positions = {}
        self.history = []

    def update(self, portfolio, prices):

        self.positions = portfolio

        total_value = self.cash

        for code, weight in portfolio.items():
            price = prices.get(code, 1)
            total_value += weight * price

        self.history.append(total_value)

        return total_value