from pay.processor import PaymentProcessor
import pytest
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'api.json')

with open(filename, "r") as file:
    API_KEY = json.load(file)[0]["API_KEY"]


def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("5555555555554444", 12, 2024, 100)


def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("5555555555554444", 12, 2024, 100)


def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("5555555555554444", 12, 1900, 100)
