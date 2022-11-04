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
    
    


emp_1 = Employee('John', "Smith")

emp_1.first = 'Jim'

# emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
