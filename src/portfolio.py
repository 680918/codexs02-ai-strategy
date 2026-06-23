import numpy as np

def build_portfolio(scores, cash=100000):

    total = sum(max(s, 0) for s in scores.values())

    weights = {}

    for k, s in scores.items():
        if s <= 0:
            weights[k] = 0
        else:
            weights[k] = s / total

    allocation = {k: cash * w for k, w in weights.items()}

    return allocation