from threading import Thread

class UnsafeCounter:
    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1

    def value(self):
        return self._counter


def task(counter):
    for _ in range(100000):
        counter.increment()


counter = UnsafeCounter()

# Creating all threads.
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]

# Starting all threads.
[thread.start() for thread in threads]

# Waiting all threads to finish up.
[thread.join() for thread in threads]

print(counter.value())
