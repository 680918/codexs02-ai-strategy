class StrategyPruner:

    def __init__(self, threshold=0.01):

        self.threshold = threshold

    def prune(self, pool, scores):

        new_pool = []

        for p in pool:

            key = str(p)

            score = scores.get(key, 0)

            if score >= self.threshold:
                new_pool.append(p)
            else:
                print("❌ 淘汰策略:", p, "score:", score)

        return new_pool