from portfolio_types import Portfolio

def validate_portfolio(p):

    # ❌ 防止 float / None
    if p is None:
        return {}

    if not isinstance(p, dict):
        return {}

    clean = {}

    for k, v in p.items():

        try:
            if isinstance(k, str) and isinstance(v, (int, float)):
                clean[k] = float(v)
        except:
            continue

    return clean