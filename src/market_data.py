import random

price_cache = {}


def get_price(code, day):

    key = f"{code}_{day}"

    if key not in price_cache:
        # 模拟真实波动
        base = 100
        price_cache[key] = base * (1 + random.uniform(-0.02, 0.02))

    return price_cache[key]