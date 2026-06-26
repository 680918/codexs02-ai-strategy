import random

price_store = {}

def get_price(code, day):

    key = f"{code}"

    if key not in price_store:
        price_store[key] = 100

    # 📈 随机游走模拟市场
    change = random.uniform(-0.02, 0.02)
    price_store[key] *= (1 + change)

    return price_store[key]