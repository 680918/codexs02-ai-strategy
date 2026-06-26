from runtime_v591 import run_v591
from evaluator_v593 import evaluate


def build_scores_from_param(param):
    """
    把参数组合转成股票评分。

    当前是简化版：
    param = (a, b, c)

    后面可以升级成：
    动量权重、资金流权重、行业轮动权重。
    """

    a, b, c = param

    scores = {
        "000001.SZ": a * 100,
        "300750.SZ": b * 100,
        "600519.SH": c * 100,
    }

    return scores


def optimize_v593(stock_data, index_data, param_grid):
    """
    v5.9.3 专用优化器。

    注意：
    不使用旧 optimizer.py
    不使用旧 backtest_engine.py
    直接调用 runtime_v591
    """

    best_param = None
    best_score = -999999

    for param in param_grid:

        scores = build_scores_from_param(param)

        equity_curve = run_v591(
            stock_data=stock_data,
            index_data=index_data,
            scores=scores
        )

        score = evaluate(equity_curve)

        print(param, "->", score)

        if score > best_score:
            best_score = score
            best_param = param

    return best_param, best_score