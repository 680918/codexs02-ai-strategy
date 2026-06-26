def run_daily(func, days=10):

    results = []

    for day in range(days):

        print(f"\n📅 Day {day+1}")

        result = func(day)

        results.append(result)

    return results

import time

def run_scheduler(run_func, rounds=5, interval_sec=2):

    print("🚀 v5.9 scheduler启动")

    for day in range(rounds):

        print(f"\n⏰ 第 {day+1} 轮执行")

        try:
            run_func(day)
        except Exception as e:
            print("❌ 执行失败:", e)

        time.sleep(interval_sec)

    print("✔ 调度结束")