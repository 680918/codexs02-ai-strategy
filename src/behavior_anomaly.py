import numpy as np


def detect_behavior(df):
    """
    主力行为识别
    """

    if len(df) < 20:
        return "数据不足"

    ret5 = df["close"].pct_change(5).iloc[-1]
    vol5 = df["vol"].pct_change(5).iloc[-1]
    vol20 = df["vol"].mean()

    # 放量
    volume_spike = vol5 > 0.5

    # 上涨
    price_up = ret5 > 0.03

    if volume_spike and price_up:
        return "🚀 主力拉升"

    if volume_spike and not price_up:
        return "📦 资金换手/洗盘"

    if not volume_spike and price_up:
        return "📈 缓慢吸筹"

    return "😐 平稳震荡"