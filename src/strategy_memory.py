class StrategyMemory:

    def __init__(self):

        # 记录每个策略的历史表现
        self.memory = {}

    def update(self, param, score):

        key = str(param)

        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(score)

    def get_weight(self, param):

        key = str(param)

        if key not in self.memory:
            return 1.0

        scores = self.memory[key]

        return sum(scores) / len(scores)