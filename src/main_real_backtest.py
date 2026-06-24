from data import load_real_data
from real_backtest_engine import run_real_backtest
from metrics import evaluate_equity_curve


def main():

    stock_data, index_data = load_real_data()

    # 先使用 v4.4/v4.5 找到的较优参数
    weights = {
        "momentum": 0.2,
        "volume": 0.5,
        "rs": 0.3
    }

    equity = run_real_backtest(
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

    print("\n===== v4.7 真实持仓回测结果 =====")
    print(f"初始资金: {equity_values[0]:.2f}")
    print(f"最终资金: {equity_values[-1]:.2f}")
    print(f"总收益率: {metrics['total_return']:.2%}")
    print(f"最大回撤: {metrics['max_drawdown']:.2%}")
    print(f"波动率: {metrics['volatility']:.4f}")
    print(f"Sharpe Ratio: {metrics['sharpe']:.4f}")

    print("\n最近5日净值:")
    for row in equity[-5:]:
        print(row)


if __name__ == "__main__":
    main()