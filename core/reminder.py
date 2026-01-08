import time
import random

number_intervals = 12
interval_duration = 1  # 1 hour in seconds


def remind(messages):
    for i in range(number_intervals):
        print("drink water")
        print(random.choice(messages))
        time.sleep(interval_duration)  # wait for 1 hour
    else:
        print("day ended and u have reached your frequent hydration needs")
