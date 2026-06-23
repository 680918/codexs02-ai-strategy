import yaml
from data import load_mock_data
from strategy import signal, score
from position import position
from backtest import Engine


def load_cfg():
    with open("configs/strategy.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run():
    data = load_mock_data()
    cfg = load_cfg()

    bt = Engine()

    for d, day in data.items():
        sig = signal(day)
        prices = {k: v["price"] for k, v in day.items()}

        for k in day:
            s = score(sig[k], cfg)
            p = position(s, cfg)

            if p > 0:
                bt.buy(k, prices[k], p)

        bt.step(prices, d)

    print("最终净值:", bt.curve[-1])


if __name__ == "__main__":
    run()