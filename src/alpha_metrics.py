# src/alpha_metrics.py

import numpy as np


def strategy_return(curve):
    return curve[-1] / curve[0] - 1


def excess_return(strategy_curve, benchmark_curve):
    return strategy_return(strategy_curve) - strategy_return(benchmark_curve)


def information_ratio(strategy_curve, benchmark_curve):

    strat_ret = np.diff(strategy_curve) / np.array(strategy_curve[:-1])
    bench_ret = np.diff(benchmark_curve) / np.array(benchmark_curve[:-1])

    diff = strat_ret - bench_ret

    if np.std(diff) == 0:
        return 0

    return np.mean(diff) / np.std(diff)


def max_drawdown(curve):

    peak = curve[0]
    mdd = 0

    for v in curve:
        peak = max(peak, v)
        dd = (peak - v) / peak
        mdd = max(mdd, dd)

    return mdd