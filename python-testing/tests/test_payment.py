from pay.order import LineItem, Order
from pay.payment import pay_order
from pytest import MonkeyPatch
from pay.credit_card import CreditCard
import pytest
from datetime import date


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging {card} with amount ${amount:.2f}.")


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("5555555555554444", 12, year)


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, card, PaymentProcessorMock())


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order, card, PaymentProcessorMock())
