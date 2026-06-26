import numpy as np


def calc_total_return(equity_curve):
    """
    总收益率
    """
    if len(equity_curve) < 2:
        return 0

    start = equity_curve[0]
    end = equity_curve[-1]

    if start == 0:
        return 0

    return end / start - 1


def calc_max_drawdown(equity_curve):
    """
    最大回撤
    """
    if len(equity_curve) == 0:
        return 0

    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        peak = max(peak, value)
        drawdown = (peak - value) / peak
        max_dd = max(max_dd, drawdown)

    return max_dd


def calc_volatility(equity_curve):
    """
    净值波动率
    """
    if len(equity_curve) < 2:
        return 0

    returns = np.diff(equity_curve) / equity_curve[:-1]

    if len(returns) == 0:
        return 0

    return np.std(returns)


def calc_sharpe(equity_curve):
    """
    简化版 Sharpe Ratio
    这里暂时不引入无风险利率
    """
    if len(equity_curve) < 2:
        return 0

    returns = np.diff(equity_curve) / equity_curve[:-1]

    if len(returns) == 0:
        return 0

    std = np.std(returns)

    if std == 0:
        return 0

    return np.mean(returns) / std


def evaluate_equity_curve(equity_curve):
    """
    综合绩效评估
    """
    return {
        "total_return": calc_total_return(equity_curve),
        "max_drawdown": calc_max_drawdown(equity_curve),
        "volatility": calc_volatility(equity_curve),
        "sharpe": calc_sharpe(equity_curve),
    }


# import numpy as np

def sharpe(returns):

    if len(returns) < 2:
        return 0

    return np.mean(returns) / (np.std(returns) + 1e-8)


def max_drawdown(values):

    peak = values[0]
    mdd = 0

    for v in values:
        peak = max(peak, v)
        dd = (peak - v) / peak
        mdd = max(mdd, dd)

    return mdd