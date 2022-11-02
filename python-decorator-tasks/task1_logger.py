# Task 1 
# Write a decorator which wraps functions to log function arguments and the return value on each call. Provide support for both positional and named arguments (your wrapper function should take both *args and **kwargs and print them both): 
from datetime import datetime

class logger:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self, *args: any, **kwargs: any) -> any:
        # Print on console
        template = f'Called Function: {str(self.func).split(" ")[1]} | Arguments: {args} {kwargs} | Result: {self.func(*args, *kwargs)}'
        print(template)
        
        # Write on File
        log = open('log.txt', 'a+')
        log.write(f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} - {template} \n')
      
@logger
def sum_2_num(a: int, b: int) -> int:
    return a + b

# mult_2_num = logger(mult_2_num)
# mult_2_num(2, 4)

@logger
def mult_2_num(a: int, b: int) -> int:
    return a * b

sum_2_num(9, 7)
mult_2_num(24, 8,)
