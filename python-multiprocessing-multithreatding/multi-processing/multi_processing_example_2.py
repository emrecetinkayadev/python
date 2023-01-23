from multiprocess import Process
import time

results = []
def longSquare(num, results: list):
    print(num**2)
    print('Finished computing!')
    results.append(num**2)



# print([longSquare(n) for n in range(0, 5)])

processes = [Process(target=longSquare, args=(n, results)) for n in range(10)]

if __name__ == "__main__":
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(results)
