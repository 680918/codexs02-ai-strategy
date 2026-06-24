# src/v49_report.py

import pandas as pd
from benchmark_engine import build_benchmark
from alpha_metrics import (
    strategy_return,
    excess_return,
    information_ratio,
    max_drawdown
)


def generate_v49_report(strategy_curve, index_data):

    benchmark_curve = build_benchmark(index_data)

    # 保证长度一致
    min_len = min(len(strategy_curve), len(benchmark_curve))
    strategy_curve = strategy_curve[:min_len]
    benchmark_curve = benchmark_curve[:min_len]

    strat_ret = strategy_return(strategy_curve)
    bench_ret = strategy_return(benchmark_curve)
    excess = excess_return(strategy_curve, benchmark_curve)
    ir = information_ratio(strategy_curve, benchmark_curve)

    strat_dd = max_drawdown(strategy_curve)
    bench_dd = max_drawdown(benchmark_curve)

    print("\n===== v4.9 Benchmark Report =====")

    print(f"策略收益:   {strat_ret:.2%}")
    print(f"基准收益:   {bench_ret:.2%}")
    print(f"超额收益:   {excess:.2%}")
    print(f"信息比率IR: {ir:.4f}")
    print(f"策略回撤:   {strat_dd:.2%}")
    print(f"基准回撤:   {bench_dd:.2%}")

    if excess > 0 and ir > 0:
        print("✔ 策略具有Alpha")
    else:
        print("⚠ 未明显跑赢市场")

    # 保存CSV
    df = pd.DataFrame({
        "strategy": strategy_curve,
        "benchmark": benchmark_curve
    })

    df.to_csv("output/benchmark_report.csv", index=False)

    print("\n📁 已生成: output/benchmark_report.csv")