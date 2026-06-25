import numpy as np
from data_guard import safe_df

def detect_accumulation(df):

    df = safe_df(df)

    if len(df) < 20:
        return "数据不足"

    ...

def detect_accumulation(df):

    if len(df) < 20:
        return "数据不足"

    vol_std = np.std(df["vol"].tail(10))
    price_range = (df["close"].max() - df["close"].min()) / df["close"].mean()

    recent_vol = df["vol"].tail(5).mean()
    past_vol = df["vol"].tail(20).mean()

    low_volatility = price_range < 0.08
    volume_slow_up = recent_vol > past_vol * 1.1

    if low_volatility and volume_slow_up:
        return "🟢 主力建仓中"

    return "⚪ 无明显建仓信号"