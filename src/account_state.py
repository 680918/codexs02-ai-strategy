class AccountState:

    def __init__(self, capital=100000):
        self.cash = capital
        self.positions = {}   # code -> amount
        self.history = []

    def update_position(self, portfolio):
        self.positions = portfolio

    def record(self, value):
        self.history.append(value)