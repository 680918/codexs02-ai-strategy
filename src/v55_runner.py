from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from real_backtest_engine import run_real_backtest


def run_v55(stock_data, index_data, scores):

    # ① 信号选股
    selected = build_signal_portfolio(stock_data)

    print("🔥 信号选股结果:", selected)

    # ② 仓位分配
    portfolio = allocate_portfolio(selected, scores)

    print("💰 仓位分配:", portfolio)

    # ③ 回测执行
    equity, trades = run_real_backtest(
        stock_data=stock_data,
        index_data=index_data,
        weights={},
        initial_capital=100000,
        top_n=len(selected) if len(selected) > 0 else 1,
        rebalance_days=5,
        fee_rate=0.001
    )

    return equity, trades, portfolio