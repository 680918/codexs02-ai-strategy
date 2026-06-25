def explain_stock(code, df):

    explanation = []

    try:
        ret = df["close"].pct_change(5).iloc[-1]
        vol = df["vol"].pct_change(5).iloc[-1]
        mom = df["close"].pct_change(10).iloc[-1]

        if ret > 0:
            explanation.append("📈 近期价格动量为正，趋势向上")
        else:
            explanation.append("📉 近期价格动量偏弱")

        if vol > 0:
            explanation.append("📊 成交量放大，资金活跃")
        else:
            explanation.append("📊 成交量较平稳")

        if mom > 0:
            explanation.append("🚀 中期趋势强于短期平均水平")
        else:
            explanation.append("⚠️ 中期趋势偏弱")

    except:
        explanation.append("数据不足，无法分析")

    return {
        "code": code,
        "explanation": explanation
    }