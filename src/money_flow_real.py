import pandas as pd
import numpy as np


def calc_real_money_flow(df):
    """
    基于真实资金流数据
    """

    if df is None or len(df) < 5:
        return 0

    try:
        main_inflow = df["buy_lg_amt"].iloc[-1]  # 大单
        super_inflow = df["buy_elg_amt"].iloc[-1]  # 超大单
        net = df["net_mf_amount"].iloc[-1]  # 净流入

        score = net * 0.5 + super_inflow * 0.3 + main_inflow * 0.2

        return score

    except:
        return 0