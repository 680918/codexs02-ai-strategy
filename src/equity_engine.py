def build_equity_curve(results, initial_capital=100000):
    """
    根据 walk-forward 的 test_score 生成简化净值曲线。

    注意：
    这里的 test_score 当前仍是简化收益评分，
    不是严格真实交易撮合后的资金曲线。
    但它可以先作为 v4.6 绩效评价的过渡版本。
    """
    equity_curve = [initial_capital]

    for r in results:
        test_score = r.get("test", initial_capital)

        if test_score is None:
            continue

        equity_curve.append(test_score)

    return equity_curve