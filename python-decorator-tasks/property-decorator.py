class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
emp_1 = Employee('John', "Smith")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())