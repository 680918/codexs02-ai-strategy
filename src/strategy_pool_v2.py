class StrategyPool:

    def __init__(self):

        self.pool = [
            (0.2, 0.3, 0.5),
            (0.3, 0.3, 0.4),
            (0.4, 0.2, 0.4),
            (0.5, 0.2, 0.3),
            (0.2, 0.5, 0.3),
        ]

        self.scores = {}

    def update_score(self, param, score):

        key = str(param)

        if key not in self.scores:
            self.scores[key] = []

        self.scores[key].append(score)

    def get_avg_score(self, param):

        key = str(param)

        if key not in self.scores:
            return 0

        return sum(self.scores[key]) / len(self.scores)