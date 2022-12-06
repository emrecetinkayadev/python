from pay.order import LineItem, Order
from pay.payment import pay_order
from pytest import MonkeyPatch
from pay.credit_card import CreditCard
import pytest


class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charging {card} with amount ${amount:.2f}.")


@pytest.fixture
def card() -> CreditCard:
    return CreditCard("5555555555554444", 12, 2024)


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    inputs = ["5555555555554444", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, PaymentProcessorMock())


def test_pay_order_invalid(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["5555555555554444", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        order = Order()
        pay_order(order, PaymentProcessorMock())
