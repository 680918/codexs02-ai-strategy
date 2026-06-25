def run_daily(func, days=10):

    results = []

    for day in range(days):

        print(f"\n📅 Day {day+1}")

        result = func(day)

        results.append(result)

    return results