import numpy as np

def calc_momentum(prices):
    return (prices[-1] / prices[-5]) - 1 if len(prices) >= 5 else 0


def calc_volume(volume):
    return np.mean(volume[-5:]) / (np.mean(volume[-20:]) + 1e-6)


def calc_relative_strength(stock_ret, index_ret):
    return stock_ret - index_ret