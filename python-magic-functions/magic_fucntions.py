
# Len method
class LenSupport:
    def __len__(self) -> int:
        return 42
    
obj = LenSupport()
print(len(obj))

class Account:
    def __init__(self, amount, owner) -> None:
        self.amount = amount