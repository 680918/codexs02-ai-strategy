from data import load_real_data
from walk_forward import walk_forward


def main():

    stock_data, index_data = load_real_data()

    results = walk_forward(stock_data, index_data)

    if len(results) == 0:
        print("⚠ 没有有效结果")
        return
    train_avg = sum(r["train"] for r in results) / len(results)
    test_avg = sum(r["test"] for r in results) / len(results)

    print("\n===== v4.5 Walk-forward结果 =====")
    print("Train平均:", train_avg)
    print("Test平均:", test_avg)

    if test_avg < train_avg:
        print("⚠ 可能存在过拟合")
    else:
        print("✔ 策略较稳定")


if __name__ == "__main__":
    main()