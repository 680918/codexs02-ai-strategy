from data import load_real_data
from optimizer import optimize


def main():

    stock_data, index_data = load_real_data()

    best_param, best_score = optimize(stock_data, index_data)

    print("\n===== v4.4 最优参数 =====")
    print(best_param)
    print("收益:", best_score)


if __name__ == "__main__":
    main()