class Engine:
    def __init__(self, cap=100000):
        self.cash = cap
        self.pos = {}
        self.curve = []

    def buy(self, k, p, w):
        amt = self.cash * w * 0.1
        self.pos[k] = self.pos.get(k, 0) + amt / p
        self.cash -= amt

    def step(self, prices, date):
        val = self.cash + sum(self.pos.get(k, 0) * prices[k] for k in prices)
        self.curve.append((date, val))