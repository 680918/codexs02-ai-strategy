
def position(score, cfg):
    if score < 30:
        return 0
    elif score < 50:
        return 0.2
    elif score < 70:
        return 0.5
    elif score < 85:
        return 0.8
    else:
        return cfg.get("max_position", 1.0)