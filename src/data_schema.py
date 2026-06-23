REQUIRED_COLUMNS = ["close", "vol"]

def validate_df(df):
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df = df.dropna()

    return df