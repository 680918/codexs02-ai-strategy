import streamlit as st

from signal_portfolio import build_signal_portfolio
from allocation_engine import allocate_portfolio
from safe_engine import validate_portfolio
from v58_engine import run_v58


# ========================
# 📦 初始化
# ========================

st.set_page_config(page_title="AI量化系统 v5.8", layout="wide")

st.title("📊 AI量化系统 v5.8（执行层可视化）")


# 假数据（你可以替换成真实 stock_data）
from data_factory import create_stock_data

stock_data = create_stock_data()

index_data = None
scores = {
    "000001.SZ": 20,
    "300750.SZ": 35,
    "600519.SH": 25
}


# ========================
# 🔥 ① 信号层
# ========================

st.header("📡 Step 1：信号生成")

if st.button("生成交易信号", key="btn_signal"):

    selected = build_signal_portfolio(stock_data)

    st.session_state["selected"] = selected

    st.write("🔥 信号股票：", selected)


# ========================
# 💰 ② 组合层
# ========================

st.header("💰 Step 2：组合构建")

if st.button("生成组合", key="btn_portfolio"):

    selected = st.session_state.get("selected", list(stock_data.keys()))

    raw_portfolio = allocate_portfolio(selected, scores, 100000)

    portfolio = validate_portfolio(raw_portfolio)

    st.session_state["portfolio"] = portfolio

    st.json(portfolio)


# ========================
# ⚙️ ③ 执行层（v5.8核心）
# ========================

st.header("⚙️ Step 3：交易执行（含滑点+冲击成本）")

if st.button("运行v5.8交易系统", key="btn_run"):

    curve = run_v58(stock_data, index_data, scores)

    st.session_state["curve"] = curve

    st.success("执行完成")


# ========================
# 📉 ④ 净值曲线展示
# ========================

st.header("📈 Step 4：净值曲线")

if "curve" in st.session_state:

    st.line_chart(st.session_state["curve"])


# ========================
# 📊 ⑤ 执行对比（核心升级）
# ========================

st.header("📊 Step 5：执行摩擦影响分析")

if st.button("生成对比", key="btn_compare"):

    ideal = [100000, 101500, 103000, 104500, 106000]

    real = st.session_state.get("curve", [])

    if len(real) == 0:
        st.warning("请先运行v5.8交易系统")
    else:
        st.line_chart({
            "Ideal（无摩擦）": ideal[:len(real)],
            "Real（含滑点+冲击）": real
        })