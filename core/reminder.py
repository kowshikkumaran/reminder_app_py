import time
import random


def remind(messages):
    i = 0
    while i < 12:
        print("drink water")
        print(random.choice(messages))
        i += 1
        time.sleep(2)  # wait for 1 hour
    else:
        print("day ended and u have reached your frequent hydration needs")
