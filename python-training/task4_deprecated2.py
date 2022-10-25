def deprecated2(new_func: any) -> any:
    def deprecated_decorator(old_func):
        def deprecated_function(*args, **kwrds):
            print(f'{old_func.__qualname__} is deprecated. {new_func.__qualname__} will be called instead.')
            return new_func(*args, **kwrds)
        return deprecated_function
    return deprecated_decorator

           
def new_foo_bar(a, b):
    return a + b - 1 

# deprecated_decorator = deprecated2(new_foo_bar)
# deprecated_function = deprecated_decorator(foo_bar)
@deprecated2(new_foo_bar)
def foo_bar(a, b):
    return a + b

print(foo_bar(3, 5))

# -------------------------- Class Version --------------------------

# class deprecated_class:
#     """
#         Deprecated class using to modifiying old codes with new ones. Do not directly call it. Instead call 'deprecated' function.
#         'deprecated' function is using as a factory pattern.
#     """
#     def __init__(self, new_func, old_func):
#         self.new_func = new_func
#         self.old_func = old_func
        
#     def __call__(self, *args, **kwrds):
#         print(f'{self.old_func.__qualname__} is deprecated. {self.new_func.__qualname__} will be called instead.')
#         return self.new_func(*args, **kwrds)
    
# # Decarator Factory
# def deprecated(new_func):
#     def deprecated_decarator(old_func):
#         return deprecated_class(new_func, old_func)
#     return deprecated_decarator

# def new_foo_bar(a, b):
#     return a + b - 1 

# @deprecated(new_foo_bar)
# def foo_bar(a, b):
#     return a + b

# print(foo_bar(3, 5)) 
