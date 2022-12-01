import threading as th
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = th.Thread(target=eat_breakfast, args=())
x.start()

y = th.Thread(target=drink_coffee, args=())
y.start()

z = th.Thread(target=study, args=())
z.start()

y.join()
x.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

print(th.active_count())
print(th.enumerate())
print(time.perf_counter())
