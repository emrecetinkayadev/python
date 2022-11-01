'''
Task 1

Implement the decorator function, which helps to count how many times
the function has occurred.

*NOTE:* NOT able to use global variables.
'''

class counter():
    _i = 0  
    def __init__(self, func) -> None:
        self.func = func
             
    def __call__(self, *args: any, **kwds: any) -> any:
        counter._i += 1
        return counter._i

@counter
def foo():
    pass

foo()
foo()
foo()

r = foo()

print(r)