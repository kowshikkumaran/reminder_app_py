import time
import random


def message():
    print("drink water")


def remind(messages):
    i = 0
    while i < 12:
        message()
        print(random.choice(messages))
        i += 1
        time.sleep(2)  # wait for 1 hour
    else:
        print("day ended and u have reached your frequent hydration needs")
