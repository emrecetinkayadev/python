# Dependency Inversion Principle
# Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.
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

# We create a different class and not force any other class to take any unused interface.(Composition Way - Interface Segregation)


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotaRobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Are you a robot? Naaaa")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):  # we delete the security_code here because we cant force an class which has different attribute then security_code, for example Paypal class using email. (Liskov Substitution.)
        pass

    # We device Payment class 2 sub classes. And Change PaymentProcessor to abstract class. (Open Close)


class DebitPaymentProcessor(PaymentProcessor,):
    def __init__(self, security_code, authorizer: Authorizer) -> None: # we changed SMSAuth to authorizer object, in this way it's not depend on child class anymore. (Dependency Inversion)
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized.")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_adress, authorizer: Authorizer) -> None:
        self.authorizer = authorizer
        self.email_adress = email_adress

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authrized.")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_adress}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = NotaRobot()
processor = DebitPaymentProcessor("hi@emre.com", authorizer)
authorizer.not_a_robot()
processor.pay(order)
