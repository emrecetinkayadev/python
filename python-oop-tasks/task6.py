'''
Task 6

Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions
(comparison, division, multiplication, addition and subtraction).
To use this methods on different currencies implement
an exchange_rate attribute.
This attribute you should be able to change according
to the currency or even delete.

'''

import functools

# @functools.total_ordering


class Money(object):
    def __init__(self, value, name) -> None:
        self.value = value
        self.name = name

    def __add__(self, other_obj):
        if isinstance(other_obj, Money):
            return Money(self.value + other_obj.value, self.name)
        else:
            raise ValueError(f"{other_obj} is not a Money type.")

    def __sub__(self, other_obj):
        if isinstance(other_obj, Money):
            return Money(self.value - other_obj.value, self.name)
        else:
            raise ValueError(f"{other_obj} is not a Money type.")

    def __mul__(self, other_obj):
        if isinstance(other_obj, Money):
            return Money(self.value - other_obj.value, self.name)
        else:
            raise ValueError(f"{other_obj} is not a Money type.")
    
    def __truediv__(self, other_obj):
        if isinstance(other_obj, Money):
            return Money(self.value - other_obj.value, self.name)
        else:
            raise ValueError(f"{other_obj} is not a Money type.")

    def __repr__(self):
        return f"Money({self.value}, '{self.name}')"

    def __getattr__(self, value):
        self.value = value


usd = Money(10, "usd")
usd_t = Money(20, "usdt")

usd_new = usd + usd_t
usd_new.exchange_rate = 0.89

usd_new2 = usd - usd_t

# print(dir(usd_new))
print(usd_new2)
print(usd_new.exchange_rate)
print(usd_new)

del usd_new.exchange_rate
print(usd_new.exchange_rate)
