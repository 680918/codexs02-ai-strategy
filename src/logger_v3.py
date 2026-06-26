class LoggerV3:

    def __init__(self):
        self.trades = []

    def log(self, day, value, portfolio):

        self.trades.append({
            "day": day,
            "value": value,
            "portfolio": portfolio
        })

    def get(self):
        return self.trades