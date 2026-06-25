def risk_control(equity_curve, positions):

    if len(equity_curve) < 2:
        return True

    drawdown = (max(equity_curve) - equity_curve[-1]) / max(equity_curve)

    # 🔴 最大回撤限制
    if drawdown > 0.1:
        print("🛑 触发风控：停止交易")
        return False

    return True


def position_limit(total_capital, exposure):

    # 单票最大仓位限制
    if exposure > total_capital * 0.3:
        return total_capital * 0.3

    return exposure