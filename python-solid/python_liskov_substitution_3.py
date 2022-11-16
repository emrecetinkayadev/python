
# Liskov Substitution Principle
# Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    # Order Class has to many responsibilities thats why we have to sperate it. (Single Responsiblity)
    # def pay(self, payment_type, security_code):


class PaymentProcessor(ABC):

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass

    # We device Payment class 2 sub classes. And Change PaymentProcessor to abstract class. (Open Close)


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized.")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code

    def auth_sms(self, code):
        raise Exception(
            "Credit card payments don't support SMS code authorization.")

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_adress) -> None:
        self.email_adress = email_adress
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authrized.")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_adress}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = CreditPaymentProcessor("hi@emre.com")
processor.pay(order)
