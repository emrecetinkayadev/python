import threading as th

x = 0


def increase():
    global x
    while x < 100:
        x = x + 1

threads = [th.Thread(target=increase, args=()) for _ in range(5)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]

print(x)
