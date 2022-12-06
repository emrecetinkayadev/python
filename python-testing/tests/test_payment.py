from pay.order import LineItem, Order
from pay.payment import pay_order, PaymentProcessor
from pytest import MonkeyPatch
import pytest


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(self, card: str, month: int, year: int, amount: int) -> None:
        pass

    inputs = ["5555555555554444", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order)


def test_pay_order_invalid(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["5555555555554444", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
        order = Order()
        pay_order(order)
