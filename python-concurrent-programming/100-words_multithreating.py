import aiohttp
import asyncio
from multiprocessing import Lock, Process, Queue, current_process, cpu_count
from threading import Thread
import requests
from time import perf_counter, sleep
from concurrent.futures import ProcessPoolExecutor
from multiprocess import Process


# ******************* Multi Threading *******************


def multi_threating():
    results = []
    URL = "https://random-word-api.herokuapp.com/word"

    # Gets a random word.
    def get_random_word() -> str:
        """gets the random word.

        Returns:
            string: random json world.
        """
        req = requests.get(url=URL)
        data = req.json()
        if not data == None:
            results.append(data)

    # Creating 10 threats.
    threat_list = [Thread(target=get_random_word) for _ in range(10)]

    start_time = perf_counter()
    [threat.start() for threat in threat_list]
    [threat.join() for threat in threat_list]
    end_time = perf_counter()

    print(results)
    print(
        f"time estimation for multi-Threading: {(end_time - start_time):.4f}")

# ******************* Multi Processing *******************


def multi_processing():

    # ******************* Multi Processing 2 *******************

    URL = "https://random-word-api.herokuapp.com/word"

    def get_random_word():
        """gets the random word.

        Returns:
            string: random json world.
        """
        req = requests.get(url=URL)
        data = req.json()
        if not data == None:
            return data

    def do_job(tasks_to_accomplish, tasks_that_are_done):
        while True:
            try:
                '''
                    try to get task from the queue. get_nowait() function will 
                    raise queue.Empty exception if the queue is empty. 
                    queue(False) function would do the same task also.
                '''
                task = tasks_to_accomplish.get_nowait()
            except queue.Empty:

                break
            else:
                '''
                    if no exception has been raised, add the task completion 
                    message to task_that_are_done queue
                '''
                print(task)
                tasks_that_are_done.put(task)
        return True

    print(f"Number of Cpu: {cpu_count()}")
    number_of_task = 10
    number_of_processes = cpu_count()
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()

    # adding tasks to queue.
    [tasks_to_accomplish.put(get_random_word) for _ in range(number_of_task)]

    # creating processes
    process_list = [Process(target=do_job, args=(
        tasks_to_accomplish, tasks_that_are_done)) for _ in range(number_of_processes)]

    start_time = perf_counter()
    [p.start() for p in process_list]
    [p.join() for p in process_list]
    end_time = perf_counter()

    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    print(
        f"time estimation for multi-Processing: {(end_time - start_time):.4f}")

# ******************* Multi Processing 2 *******************


def multi_processing_2():
    URL = "https://random-word-api.herokuapp.com/word"
    # Gets a random word.

    def get_random_word() -> str:
        """gets the random word.

        Returns:
            string: random json world.
        """
        req = requests.get(url=URL)
        data = req.json()
        if not data == None:
            print(data)

    processes = [Process(target=get_random_word) for _ in range(10)]

    start_time = perf_counter()
    [p.start() for p in processes]
    [p.join() for p in processes]
    end_time = perf_counter()

    print(
        f"time estimation for multi-Threading: {(end_time - start_time):.4f}")

# ******************* Async / Await *******************


async def async_await():
    URL = "https://random-word-api.herokuapp.com/word"

    async def get_random_word():
        """gets the random word.

        Returns:
            string: random json world.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                data = await resp.json()
                if data:
                    return data

    # Creating a list of tasks
    tasks = [asyncio.create_task(get_random_word()) for _ in range(10)]

    start_time = perf_counter()
    # Running the tasks concurrently
    results = await asyncio.gather(*tasks)
    end_time = perf_counter()

    print(results)
    print(f"time estimation for asyncio: {(end_time - start_time):.4f}")


if __name__ == "__main__":
    # multi_threating()
    # multi_processing()
    multi_processing_2()
    # asyncio.run(async_await())
