import numpy as np

def detect_anomaly(df):

    if len(df) < 10:
        return "数据不足"

    ret5 = df["close"].pct_change(5).iloc[-1]
    vol5 = df["vol"].pct_change(5).iloc[-1]

    volatility = np.std(df["close"].pct_change().tail(10))

    if vol5 > 0.5 and ret5 > 0.03:
        return "🚨 强异动（可能启动）"

    if vol5 > 0.5 and ret5 < 0:
        return "⚠ 放量下跌（可能出货）"

    if volatility > 0.03:
        return "⚡ 波动率异常"

    return "正常"