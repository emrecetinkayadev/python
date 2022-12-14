class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name: str):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        print(f"Setter Ran, value: {name}")

    @fullname.deleter
    def fullname(self):
        print(f'{self.first} {self.last} deleted.')
        self.first = None
        self.last = None
        print("Deleter Ran")


emp_1 = Employee('John', "Smith")

emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)
