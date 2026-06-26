from data_factory import create_stock_data
from strategy_pool import STRATEGY_POOL
from optimizer_v2 import optimize_v593


def main():

    print("\n🚀 v5.9.3 策略优化系统启动")

    stock_data = create_stock_data()
    index_data = None

    best_param, best_score = optimize_v593(
        stock_data=stock_data,
        index_data=index_data,
        param_grid=STRATEGY_POOL
    )

    print("\n===== v5.9.3 最优结果 =====")
    print("最优参数:", best_param)
    print("最优得分:", best_score)


if __name__ == "__main__":
    main()