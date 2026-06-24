def calc_trade_cost(amount, fee_rate=0.001):
    """
    简化交易成本：
    默认千分之一，包含佣金、滑点、冲击成本的粗略估计。
    """
    return amount * fee_rate