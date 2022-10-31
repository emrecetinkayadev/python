# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():
    def __init__(self, name) -> None:
        self.name = name
        


# TODO: create instances of the class
b1 = Book("Alice in Wonderland")
b2 = Book("Lord of the Rings")

# TODO: print the class and property
print(f'Book1 :{b1.name} Class Name: {b1.__ne__}')
