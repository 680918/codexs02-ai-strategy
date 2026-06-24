import os
import pandas as pd


OUTPUT_DIR = "output"


def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def export_equity_curve(equity_curve, filename="equity_curve.csv"):
    ensure_output_dir()

    df = pd.DataFrame(equity_curve, columns=["trade_date", "equity"])
    path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(path, index=False, encoding="utf-8-sig")

    return path


def export_trades(trades, filename="trades.csv"):
    ensure_output_dir()

    df = pd.DataFrame(trades)
    path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(path, index=False, encoding="utf-8-sig")

    return path


def export_summary(summary_text, filename="report_summary.txt"):
    ensure_output_dir()

    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(summary_text)

    return path