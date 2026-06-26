from scheduler import run_scheduler
from runtime_engine import run_runtime


def main():

    def step(day):
        run_runtime({}, {}, {}, day)

    run_scheduler(step, rounds=5, interval_sec=2)


if __name__ == "__main__":
    main()