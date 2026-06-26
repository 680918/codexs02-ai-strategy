from data_factory import create_stock_data
from strategy_pool import STRATEGY_POOL
from evolution_engine import evolve


def main():

    print("\n🧬 v5.9.4 策略进化系统启动")

    stock_data = create_stock_data()
    index_data = None

    best_param, best_score = evolve(
        stock_data,
        index_data,
        STRATEGY_POOL
    )

    print("\n===== v5.9.4 最终进化结果 =====")
    print("最优参数:", best_param)
    print("得分:", best_score)


if __name__ == "__main__":
    main()