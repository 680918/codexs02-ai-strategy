def generate_report(curve, logs):

    print("\n===== v4.3.2 回测报告 =====")

    print(f"日志条数: {len(logs)}")

    if curve is None or len(curve) == 0:
        print("⚠ 无净值曲线（v4.3组合模式未生成curve）")
        return

    start = curve[0][1]
    end = curve[-1][1]

    ret = (end / start - 1) * 100

    print(f"收益率: {ret:.2f}%")