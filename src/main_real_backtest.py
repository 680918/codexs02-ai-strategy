from data import load_real_data
from real_backtest_engine import run_real_backtest
from metrics import evaluate_equity_curve
from exporter import export_equity_curve, export_trades, export_summary


def main():

    stock_data, index_data = load_real_data()

    weights = {
        "momentum": 0.2,
        "volume": 0.5,
        "rs": 0.3
    }

    equity, trades = run_real_backtest(
        stock_data=stock_data,
        index_data=index_data,
        weights=weights,
        initial_capital=100000,
        top_n=2,
        rebalance_days=5,
        fee_rate=0.001
    )

    equity_values = [x[1] for x in equity]
    metrics = evaluate_equity_curve(equity_values)

    print("\n===== v4.8 真实持仓回测结果 =====")
    print(f"初始资金: {equity_values[0]:.2f}")
    print(f"最终资金: {equity_values[-1]:.2f}")
    print(f"总收益率: {metrics['total_return']:.2%}")
    print(f"最大回撤: {metrics['max_drawdown']:.2%}")
    print(f"波动率: {metrics['volatility']:.4f}")
    print(f"Sharpe Ratio: {metrics['sharpe']:.4f}")

    print("\n最近5日净值:")
    for row in equity[-5:]:
        print(row)

    equity_path = export_equity_curve(equity)
    trades_path = export_trades(trades)

    summary = f"""
===== v4.8 回测摘要 =====

初始资金: {equity_values[0]:.2f}
最终资金: {equity_values[-1]:.2f}
总收益率: {metrics['total_return']:.2%}
最大回撤: {metrics['max_drawdown']:.2%}
波动率: {metrics['volatility']:.4f}
Sharpe Ratio: {metrics['sharpe']:.4f}

交易次数: {len(trades)}

输出文件:
- {equity_path}
- {trades_path}
"""

    summary_path = export_summary(summary)

    print("\n===== v4.8 文件导出 =====")
    print("净值曲线:", equity_path)
    print("交易记录:", trades_path)
    print("摘要报告:", summary_path)


if __name__ == "__main__":
    main()