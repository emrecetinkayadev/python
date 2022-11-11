
# 1. Single Responsibility
# A class should have one and only one reason to change, meaning that a class should have only one job.

class Order:
    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    # Order Class has to many responsibilities thats why we have to sperate it.
    # def pay(self, payment_type, security_code):


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")

order2 = Order()
order2.add_item("ee", 2, 23)
order2.add_item("aa", 1, 15)
order2.add_item("bb", 2, 5)
print(order2.total_price())
