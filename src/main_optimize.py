from data import load_real_data
from walk_forward import walk_forward
from equity_engine import build_equity_curve
from metrics import evaluate_equity_curve


def main():

    stock_data, index_data = load_real_data()

    results = walk_forward(stock_data, index_data)

    if len(results) == 0:
        print("⚠ 没有有效walk-forward结果")
        return

    train_avg = sum(r["train"] for r in results) / len(results)
    test_avg = sum(r["test"] for r in results) / len(results)

    equity_curve = build_equity_curve(results)
    metrics = evaluate_equity_curve(equity_curve)

    print("\n===== v4.5 Walk-forward结果 =====")
    print("Train平均:", train_avg)
    print("Test平均:", test_avg)

    print("\n===== v4.6 投资绩效指标 =====")
    print(f"总收益率: {metrics['total_return']:.2%}")
    print(f"最大回撤: {metrics['max_drawdown']:.2%}")
    print(f"波动率: {metrics['volatility']:.4f}")
    print(f"Sharpe Ratio: {metrics['sharpe']:.4f}")

    print("\n===== v4.6 稳定性判断 =====")

    if metrics["sharpe"] > 1 and metrics["max_drawdown"] < 0.2:
        print("✔ 策略稳定性较好")
    elif metrics["sharpe"] > 0 and metrics["max_drawdown"] < 0.3:
        print("⚠ 策略有一定效果，但稳定性一般")
    else:
        print("❌ 策略稳定性较弱，需要继续优化")

    if test_avg < train_avg:
        print("⚠ Test弱于Train，可能存在过拟合")
    else:
        print("✔ Test不弱于Train，参数稳定性较好")


if __name__ == "__main__":
    main()