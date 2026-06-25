from signal_engine import generate_signals


def build_signal_portfolio(stock_data):

    selected = []

    for code, df in stock_data.items():

        signal = generate_signals(df)

        if "强买入" in signal or "潜在吸筹" in signal:
            selected.append(code)

    return selected