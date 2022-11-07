
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

#__len__, __getitem__, __reversed__


class Account_New(Account):
    def __init__(self, owner, amount=0) -> None:
        super().__init__(owner, amount)
        self._transections = []

    def __len__(self):
        return len(self._transections)

    def __getitem__(self, position):
        return self._transections[position]

    def add_amount(self, amount) -> None:
        if not isinstance(amount, int):
            raise ValueError(f'{amount} is not a int type.')
        else:
            self._transections.append(amount)

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transections)


accbob = Account_New("Bob", 10)
accbob.add_amount(20)
accbob.add_amount(-30)
accbob.add_amount(60)
print(accbob.balance)

print(len(accbob))
for amount in accbob:
    print(amount)

if 20 in accbob:
    print(True)

print(dir(accbob))
