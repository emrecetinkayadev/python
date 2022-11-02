# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ["HARDCOVER", "COMIC"]

    # TODO: double-underscore properties are hidden from other classes
    __bookList = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getBookList():
        if Book.__bookList == None:
            Book.__bookList = []
        return Book.__bookList
    
    @staticmethod
    def addBookList(book):
        booklist = Book.getBookList()
        booklist.append(book)


    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        Book.addBookList(title)
        
        # Book Type Check
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f'Not in the spesific Book Types.')
        else:
            self.booktype = booktype


# TODO: access the class attribute


# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "COMIC")
b3 = Book("Title 2", "COMIC")


# TODO: Use the static method to access a singleton object
print(Book.getBookList())