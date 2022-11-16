import threading
import time


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
# print([longSquare(n) for n in range(0, 5)])

t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))

t1.start()
t2.start()

t2.join()
t1.join()

print(results)
