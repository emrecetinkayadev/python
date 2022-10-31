# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price, secretkey = "AAS"):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = secretkey

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return format(self.price - (self.price * self._discount),'.2f')
        return self.price
    
    def setDiscount(self, discount):
        self._discount = discount


# TODO: create some book instances
b1 = Book("War and Peace", "Emre", 320, 50, "AAB")
b2 = Book("The Catcher in the Rye", "G.Morgan", 500, 29)

# TODO: print the price of book1
print(b1.getPrice())
print(b2.getPrice())

# TODO: try setting the discount
b1.setDiscount(0.23443435)
print(b1.getPrice())


# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)
print(b2._Book__secret)