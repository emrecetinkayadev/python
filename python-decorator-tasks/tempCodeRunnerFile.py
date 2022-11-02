from functools import reduce

price_map = {'orange': 10, 'apple': 20}
items = ['orange', 'apple']

def deprecated(new_func):
    def deprecated_decarator(old_func):
        def deprecated_function(*args, **kwrds):
            new_func(*args, **kwrds)
        return deprecated_function
    return deprecated_decarator

def total_val_new():
    return reduce(lambda x,y: price_map[x] + price_map[y], items)

@deprecated(total_val_new)
def totalVal():
    total_price = 0
    for item in items:
        total_price += price_map.get(item)
    return total_price

print(totalVal())