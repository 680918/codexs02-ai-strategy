import numpy as np

def execute_order(price, amount, liquidity=1e6, slippage=0.002):

    # ① 流动性限制（冲击成本）
    impact = amount / liquidity
    impact_cost = price * impact

    # ② 滑点
    slip = price * slippage

    exec_price = price + impact_cost + slip

    return exec_price