def position(score, cfg):
    if score < cfg["sell_threshold"]:
        return 0
    if score < cfg["buy_threshold"]:
        return 0.3
    return cfg["max_position"]