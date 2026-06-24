# src/benchmark_engine.py

import numpy as np

def build_benchmark(index_data, initial_capital=100000):
    """
    用指数收益生成基准净值曲线
    """

    equity = [initial_capital]

    returns = index_data["close"].pct_change().fillna(0)

    for r in returns:
        equity.append(equity[-1] * (1 + r))

    return equity


def get_benchmark_return(benchmark_curve):
    return benchmark_curve[-1] / benchmark_curve[0] - 1