import streamlit as st
import pandas as pd
import numpy as np

from data import load_real_data
from real_backtest_engine import run_real_backtest
from v49_report import generate_v49_report
from hotspot_engine import get_top_hotspots
from ai_explainer import explain_stock
from money_flow import get_top_money_flow
from sector_rotation import get_hot_sectors
from data_tushare import get_stock_data, get_moneyflow
from money_flow_real import calc_real_money_flow
from behavior_anomaly import detect_behavior

# ======================
# 页面配置
# ======================
st.set_page_config(page_title="AI量化系统v5.0", layout="wide")

st.title("📊 AI量化策略系统 v5.0")


# ======================
# 数据加载
# ======================
stock_data, index_data = load_real_data()


# ======================
# 侧边栏参数
# ======================
st.sidebar.header("⚙ 策略参数")

top_n = st.sidebar.slider("选股数量 Top N", 1, 5, 2)
rebalance = st.sidebar.slider("调仓周期", 1, 10, 5)
fee = st.sidebar.slider("手续费", 0.0, 0.01, 0.001)


run_btn = st.sidebar.button("🚀 运行回测")


# ======================
# 运行回测
# ======================
if run_btn:

    weights = {
        "momentum": 0.2,
        "volume": 0.5,
        "rs": 0.3
    }

    equity, trades = run_real_backtest(
        stock_data=stock_data,
        index_data=index_data,
        weights=weights,
        initial_capital=100000,
        top_n=top_n,
        rebalance_days=rebalance,
        fee_rate=fee
    )

    equity_values = [x[1] for x in equity]


    # ======================
    # 📊 收益曲线
    # ======================
    st.subheader("📈 净值曲线")

    df_curve = pd.DataFrame(equity, columns=["date", "equity"])
    st.line_chart(df_curve.set_index("date"))


    # ======================
    # 📊 绩效指标
    # ======================
    st.subheader("📊 回测结果")

    total_return = equity_values[-1] / equity_values[0] - 1
    max_dd = min(equity_values) / max(equity_values) - 1

    col1, col2, col3 = st.columns(3)

    col1.metric("总收益率", f"{total_return:.2%}")
    col2.metric("最大回撤", f"{max_dd:.2%}")
    col3.metric("交易次数", len(trades))


    # ======================
    # 📊 Benchmark（v4.9）
    # ======================
    st.subheader("📊 Alpha分析（vs沪深300）")

    report = generate_v49_report(equity_values, index_data)

    st.success("✔ Benchmark分析完成")


    # ======================
    # 📌 交易记录
    # ======================
    st.subheader("📌 交易记录")

    if len(trades) > 0:
        df_trades = pd.DataFrame(trades)
        st.dataframe(df_trades)
    else:
        st.warning("暂无交易记录")

    st.subheader("🔥 热点板块选股")

hot_btn = st.button("生成热点股票")

if hot_btn:

    hotspots = get_top_hotspots(stock_data, top_n=5)

    st.dataframe(hotspots)

    st.session_state["hotspots"] = hotspots

st.subheader("🧠 AI选股解释")

if "hotspots" in st.session_state:

    selected = st.selectbox(
        "选择股票查看解释",
        st.session_state["hotspots"]["code"].tolist()
    )

    df = stock_data[selected]

    result = explain_stock(selected, df)

    st.write("### 📌 解释逻辑")

    for line in result["explanation"]:
        st.write(line)

st.subheader("💰 主力资金流分析")

if st.button("分析资金流"):

    mf = get_top_money_flow(stock_data, 5)

    st.dataframe(mf)

st.subheader("📊 行业轮动")

if st.button("分析行业强度"):

    sectors = get_hot_sectors(stock_data)

    st.dataframe(sectors)

st.subheader("💰 真实资金流分析（v5.3）")

stock = st.selectbox("选择股票", list(stock_data.keys()))

if st.button("分析主力行为"):

    df = stock_data[stock]

    behavior = detect_behavior(df)

    st.write("### 🧠 主力行为判断")
    st.success(behavior)

st.subheader("📊 真实资金流评分")

if st.button("计算资金流"):

    mf = get_moneyflow(stock)

    score = calc_real_money_flow(mf)

    st.metric("资金流强度", f"{score:.2f}")


# ======================
# 默认展示说明
# ======================
else:
    st.info("点击左侧按钮运行回测")