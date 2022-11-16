import threading
import time


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}

thread = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 1000)]

[t.start() for t in thread]
[t.join() for t in thread]

print(results)
