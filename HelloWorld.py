from numpy import var


class Account:
    # Variables
    owner: str
    amount: float

    # Constructor
    def __init__(self, owner: str, amount: float) -> None:
        self.owner = owner
        self.amount = amount

    # Methods
    def deposit(self, amount: float):
        self.amount += amount

    def withdraw(self, amount: float):
        self.amount -= amount

    def inquiry(self) -> float:
        return self.amount

    def __repr__(self) -> str:
        return f'Account({self.owner},{self.amount})'


print("Hello Python and Git World!")
print("Looping in Python")
x = 1
while x <= 5:
    print(x)
    x += 1

print("Object Oriented Programming")
a = Account("Iminathi", 1000)
print(vars(a))
