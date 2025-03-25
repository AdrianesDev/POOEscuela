from Book import Book
class Library:

    def __init__(self):
       self.catalog = []

    def addBook(self,book:Book):
        self.catalog.append(book)

    def findBook(self,title):
        for book in self.catalog:
            if book.title == title:
                return book
            else: "Book doesn't exist"

    def showAvailableBooks(self):
        books = [book for book in self.catalog if not book.isBorrowed]
        if books:
            print("Available books:")
            for book in books:
                print(book.description())
        else:
            print("No available books.")

    def showAllBooks(self):
        print("All our books:")
        books = [book for book in self.catalog]
        for book in books:
            print(book.description())