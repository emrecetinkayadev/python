from dataclasses import dataclass


@dataclass
class CreditCard:
    number: str
    expiry_year: str
    expiry_month: str
