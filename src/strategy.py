def signal(day):
    out = {}
    for k, v in day.items():
        out[k] = {
            "momentum": v["momentum"],
            "volume": v["volume"],
            "trend": 0.6
        }
    return out


def score(sig, cfg):
    return (
        sig["momentum"] * cfg["weights"]["momentum"] +
        sig["volume"] * cfg["weights"]["volume"] +
        sig["trend"] * cfg["weights"]["trend"]
    )