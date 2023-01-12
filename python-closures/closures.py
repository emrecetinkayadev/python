
def inner():
    x = 10

    def outer():
        nonlocal x
        x = x + 1
        return x
    return outer


increment = inner()

print(increment())
print(increment())
print(increment())
