import numpy as np


def allocate_portfolio(selected, scores, total_capital=100000):

    if len(selected) == 0:
        return {}

    # softmax式分配（更机构化）
    weights = np.array([scores.get(s, 1) for s in selected])
    weights = np.exp(weights) / np.sum(np.exp(weights))

    portfolio = {}

    for i, code in enumerate(selected):
        portfolio[code] = total_capital * weights[i]

    return portfolio