import time


def drink():
    print("drink water")


i = 0
while i < 12:
    drink()
    i += 1
    time.sleep(60 * 60)  # wait for 1 hour
else:
    print("day ended and u have reached your frequent hydration needs")
