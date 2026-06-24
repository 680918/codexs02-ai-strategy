import itertools
from backtest_engine import run_backtest


def generate_params():
    space = [0.2, 0.3, 0.4, 0.5]

    for w1, w2, w3 in itertools.product(space, repeat=3):
        if abs(w1 + w2 + w3 - 1.0) < 0.01:
            yield {
                "momentum": w1,
                "volume": w2,
                "rs": w3
            }


def optimize(stock_data, index_data):

    best_score = -999999
    best_param = None

    for params in generate_params():

        result = run_backtest(stock_data, index_data, params)

        print(params, "->", result)

        if result > best_score:
            best_score = result
            best_param = params

    return best_param, best_score