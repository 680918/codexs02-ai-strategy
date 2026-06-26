import numpy as np


def calc_returns(equity_curve):
    if len(equity_curve) < 2:
        return []

    returns = []

    for i in range(1, len(equity_curve)):
        prev = equity_curve[i - 1]
        curr = equity_curve[i]

        if prev == 0:
            returns.append(0)
        else:
            returns.append((curr - prev) / prev)

    return returns


def calc_sharpe(equity_curve):
    returns = calc_returns(equity_curve)

    if len(returns) < 2:
        return 0

    mean_ret = np.mean(returns)
    std_ret = np.std(returns)

    if std_ret == 0:
        return 0

    return mean_ret / std_ret


def calc_max_drawdown(equity_curve):
    if len(equity_curve) == 0:
        return 0

    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        peak = max(peak, value)

        if peak == 0:
            continue

        dd = (peak - value) / peak
        max_dd = max(max_dd, dd)

    return max_dd


def evaluate(equity_curve):
    """
    v5.9.3 策略评分函数：
    Sharpe 越高越好，最大回撤越低越好。
    """

    sharpe = calc_sharpe(equity_curve)
    mdd = calc_max_drawdown(equity_curve)

    score = sharpe - mdd

    return score