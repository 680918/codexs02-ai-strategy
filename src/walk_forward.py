from optimizer import generate_params
from backtest_engine import run_backtest


def walk_forward(stock_data, index_data, window=10, step=3):

    results = []

    dates = list(stock_data[list(stock_data.keys())[0]].index)

    for start in range(0, len(dates) - window - step, step):

        train_start = start
        train_end = start + window
        test_end = start + window + step

        train_data = slice_data(stock_data, train_start, train_end)
        test_data = slice_data(stock_data, train_end, test_end)

        best_params = None
        best_score = -999999

        # 🟢 train阶段（找参数）
        for params in generate_params():

            score = run_backtest(train_data, index_data, params)

            if score > best_score:
                best_score = score
                best_params = params

        # 🟢 test阶段（验证）
        test_score = run_backtest(test_data, index_data, best_params)

        results.append({
            "train": best_score,
            "test": test_score,
            "params": best_params
        })

        print("WF window:", start, "test_score:", test_score)
        print("数据长度:", len(dates))
        print("window:", window)
        print("step:", step)

    return results

def slice_data(stock_data, start, end):

    sliced = {}

    for k, df in stock_data.items():
        sliced[k] = df.iloc[start:end]

    return sliced