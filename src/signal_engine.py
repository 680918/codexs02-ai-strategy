from accumulation_detector import detect_accumulation
from anomaly_alert import detect_anomaly
from data_guard import safe_df

def generate_signals(df):

    df = safe_df(df)

    acc = detect_accumulation(df)


def generate_signals(df):

    acc = detect_accumulation(df)
    ano = detect_anomaly(df)

    if "建仓" in acc and "异动" in ano:
        return "🔥 强买入信号"

    if "建仓" in acc:
        return "📊 潜在吸筹区"

    if "异动" in ano:
        return "⚠ 风险/机会并存"

    return "😐 无明确信号"