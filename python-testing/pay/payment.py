from pay.credit_card import CreditCard
from pay.order import Order
from typing import Protocol

class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """Charges the card with the amount.

        Args:
            card (str): _description_
            month (int): _description_
            year (int): _description_
            amount (int): _description_
        """


def pay_order(order: Order, card: CreditCard, processor: PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    processor.charge(card, amount=order.total)
    order.pay()
