# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))

# ----------------------------------------

def counter(func):
    def helper(*args, **kwrd):
        helper.calls += 1
        print(helper.calls)
        return func(*args, **kwrd)
    helper.calls = 0
    return helper

@counter
def hello():
    print("hello word!")

hello()
hello()
hello()
hello()

#----------------------------------------------

class CallCountDecorator:
    """
    A decorator that will count and print how many times the decorated function was called
    """

    def __init__(self, inline_func):
        self.call_count = 0
        self.inline_func = inline_func

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        self._print_call_count()
        return self.inline_func(*args, **kwargs)

    def _print_call_count(self):
        print(f"The {self.inline_func.__name__} called {self.call_count} times")

#new_func = CallCountDecorator(function)
@CallCountDecorator
def function():
    pass


@CallCountDecorator
def function2(a, b):
    pass

function()
function2(1, b=2)
function()
function2(a=2, b=3)
function2(0, 1)



# def call_counter(func):
#     def helper(*args, **kwargs):
#         helper.calls += 1
#         print(helper.calls)
#         return func(*args, **kwargs)
#     helper.calls = 0
#     return helper

# @call_counter
# def succ(x):
#     return x + 1

# succ(2)
# succ(2)
# succ(2)
# succ(2)
