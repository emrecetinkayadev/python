
# __len__ method
class LenSupport:
    def __len__(self) -> int:
        return 42


obj = LenSupport()
print(len(obj))


# __init__ method
class Account:
    def __init__(self, owner, amount=0) -> None:
        self.amount = amount
        self.owner = owner


acc1 = Account("Emre")  #  amount = 0 default
acc2 = Account("Henry", 100)

print(acc1.amount, acc2.amount)


# __str__ , __repr__ methods.
class Account_str(Account):
    def __str__(self) -> str:
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self) -> str:
        return f'Account("{self.owner}", {self.amount})'


acc_str = Account_str("Helena")
print(str(acc_str))
print(repr(acc_str))
print(acc_str)
