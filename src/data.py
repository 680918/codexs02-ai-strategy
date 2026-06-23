import numpy as np
import pandas as pd

def load_mock_data():
    dates = pd.date_range("2024-01-01", periods=60)
    data = {}

    for i, d in enumerate(dates):
        data[str(d.date())] = {
            "A": {"price": 10+i*0.1, "momentum": np.random.randn(), "volume": 1+np.random.rand()},
            "B": {"price": 20+i*0.1, "momentum": np.random.randn(), "volume": 1+np.random.rand()}
        }

    return data