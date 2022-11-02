import hashlib

class Cache:
    def __init__(self, func) -> None:
        self.func = func
        self.cache = {}
        
    def __call__(self, *args: any, **kwds: any) -> any:
        # Inputs; we are hashing given inputs as a keywords for our Hash Table.       
        hash = hashlib.sha256()
        hash.update(str(*args, **kwds).encode('utf-8'))
        hashed_args = hash.hexdigest()

        # Checking if existing key is in our Hash Table, if yes return result, if no operate function.
        if hashed_args in self.cache:
            return self.cache[hashed_args]
        else:
            result = self.cache[hashed_args] = self.func(*args, **kwds)
            return result

# fib(call function) = Cache(fibonacci)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
@Cache
def fibonacci(n):
    if n == 0 | n == 1:
        return 1
    elif n < 0:
        return 0
    print(f'Fibonacci: {fibonacci(n-1) + fibonacci(n-2)}')
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))



    