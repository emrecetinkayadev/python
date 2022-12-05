from threading import Thread
from threading import Lock
from time import perf_counter


class ThreadSafeCounter:
    def __init__(self) -> None:
        self._counter = 0
        self._lock = Lock()

    def increment(self):
        # Faster.
        # self._lock.acquire()
        # self._counter += 1
        # self._lock.release()

        with self._lock:
            self._counter += 1

    def value(self):
        return self._counter


def task(counter):
    for _ in range(100000):
        counter.increment()


counter = ThreadSafeCounter()

# For performance check
start_time = perf_counter()

# Creating all threads.
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]

# Starting all threads.
[thread.start() for thread in threads]

# Waiting all threads to finish.
[thread.join() for thread in threads]

print(counter.value(), f"Performance time: {perf_counter() - start_time}")
