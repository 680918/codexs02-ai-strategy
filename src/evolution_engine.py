from strategy_memory import StrategyMemory
from runtime_v591 import run_v591
from evaluator_v593 import evaluate


def evolve(stock_data, index_data, param_grid):

    memory = StrategyMemory()

    best_param = None
    best_score = -999999

    for epoch in range(3):  # 多轮进化

        print(f"\n🧬 Epoch {epoch}")

        for param in param_grid:

            scores = {
                "000001.SZ": param[0] * 100,
                "300750.SZ": param[1] * 100,
                "600519.SH": param[2] * 100,
            }

            equity = run_v591(stock_data, index_data, scores)

            score = evaluate(equity)

            memory.update(param, score)

            # 🧠 加权评分（记忆影响）
            weight = memory.get_weight(param)

            final_score = score * weight

            print(param, "score:", score, "weighted:", final_score)

            if final_score > best_score:
                best_score = final_score
                best_param = param

    return best_param, best_score