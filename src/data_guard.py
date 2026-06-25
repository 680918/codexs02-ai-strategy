import pandas as pd

def safe_df(df):

    # ❌ 防 None
    if df is None:
        return pd.DataFrame(columns=["close", "vol"])

    # ❌ 防类型错误
    if not isinstance(df, pd.DataFrame):
        return pd.DataFrame(columns=["close", "vol"])

    # ❌ 防缺字段
    if "close" not in df.columns:
        df["close"] = 100

    if "vol" not in df.columns:
        df["vol"] = 1000

    # ❌ 防空数据
    if len(df) == 0:
        return pd.DataFrame(columns=["close", "vol"])

    return df