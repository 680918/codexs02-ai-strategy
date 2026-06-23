def risk_adjust(weight, score):

    if score < 30:
        return weight * 0.2
    elif score < 50:
        return weight * 0.5
    elif score < 70:
        return weight * 0.8
    else:
        return weight