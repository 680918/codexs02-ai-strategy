from strategy_pool_v2 import StrategyPool
from pruner import StrategyPruner
from runtime_v591 import run_v591
from evaluator_v593 import evaluate
from data_factory import create_stock_data


def main():

    print("\n🧠 v5.9.5 策略淘汰系统启动")

    pool = StrategyPool()
    pruner = StrategyPruner(threshold=0.02)

    stock_data = create_stock_data()
    index_data = None

    for epoch in range(3):

        print(f"\n📊 Epoch {epoch}")

        results = {}

        for param in pool.pool:

            scores = {
                "000001.SZ": param[0] * 100,
                "300750.SZ": param[1] * 100,
                "600519.SH": param[2] * 100,
            }

            equity = run_v591(stock_data, index_data, scores)

            score = evaluate(equity)

            pool.update_score(param, score)

            results[str(param)] = pool.get_avg_score(param)

        # 🧠 淘汰步骤（核心）
        pool.pool = pruner.prune(pool.pool, results)

        print("✔ 当前策略池:", pool.pool)

    print("\n===== v5.9.5结束 =====")
    print("最终策略池:", pool.pool)


if __name__ == "__main__":
    main()