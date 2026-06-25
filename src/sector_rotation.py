import pandas as pd
import numpy as np

# 简化行业映射（你后面可以接 tushare industry）
SECTOR_MAP = {
    "600": "大金融",
    "601": "大金融",
    "000": "消费",
    "300": "成长",
}


def infer_sector(code):
    prefix = code[:3]
    return SECTOR_MAP.get(prefix, "其他")


def sector_rotation(stock_data):
    """
    行业轮动分析
    """

    sector_scores = {}

    for code, df in stock_data.items():

        if len(df) < 20:
            continue

        sector = infer_sector(code)

        try:
            ret = df["close"].pct_change(10).iloc[-1]
            vol = df["vol"].pct_change(10).iloc[-1]

            score = ret * 0.7 + vol * 0.3

            if sector not in sector_scores:
                sector_scores[sector] = []

            sector_scores[sector].append(score)

        except:
            continue

    # 聚合行业强度
    result = []

    for sector, scores in sector_scores.items():

        result.append({
            "sector": sector,
            "strength": np.mean(scores),
            "stocks_count": len(scores)
        })

    return pd.DataFrame(result).sort_values("strength", ascending=False)


def get_hot_sectors(stock_data):
    return sector_rotation(stock_data)