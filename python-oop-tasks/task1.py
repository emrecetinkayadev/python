'''
Task 1

Implement the decorator function, which helps to count how many times
the function has occurred.

*NOTE:* NOT able to use global variables.
'''

class Counter():
    _i = 0  
    def __init__(self, func) -> None:
        self.func = func
             
    def __call__(self, *args: any, **kwds: any) -> any:
        Counter._i += 1
        return Counter._i

@Counter
def foo():
    pass

@Counter
def foo1():
    pass


foo()
foo()
foo()
foo1()

r = foo()

print(r)