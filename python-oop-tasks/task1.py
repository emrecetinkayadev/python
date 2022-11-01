
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