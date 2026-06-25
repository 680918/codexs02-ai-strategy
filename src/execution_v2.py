def execute_trade(price, amount, liquidity=1e6):

    # 📉 流动性冲击
    impact = amount / liquidity

    # 📊 非线性冲击成本（更真实）
    slippage = price * (0.001 + impact ** 2)

    exec_price = price + slippage

    return exec_price