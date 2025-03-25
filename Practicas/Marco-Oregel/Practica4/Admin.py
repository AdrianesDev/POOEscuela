from RoleProtocol import RoleProtocol
from Book import Book

class Admin(RoleProtocol):
    def __init__(self, name, username, password):
        super().__init__(name)
        self._username = username
        self._password = password
        self.catalog = []

    def loginProcess(self):
         print(f"{self._username} has logged in, Welcome {self._name}!")

    def addBook(self,book:Book):
        self.catalog.append(book)
        print(f"{self._name} added : {book.title} successfully!")
    def removeBook(self,book:Book):
        self.catalog.remove(book)
        print(f"{self._name} removed : {book.title} successfully!")
    
    def showAllBooks(self):
        print("All our books:")
        books = [book for book in self.catalog]
        for book in books:
            print(book.description())

    def showAvailableBooks(self):
        books = [book for book in self.catalog if not book.isBorrowed]
        if books:
            print("Available books:")
            for book in books:
                print(book.description())
        else:
            print("No available books.")
    
    def findBook(self,title):
        for book in self.catalog:
            if book.title == title:
                print("Book Found:")
                print(book.description())
            else: "Book doesn't exist"
        

    def logOutProcess(self):
         print(f"{self._username} has logged out, See you later!")

