from Book import Book
from RoleProtocol import RoleProtocol
class User(RoleProtocol):

    def __init__(self, name, username, password,admin):
       super().__init__(name)
       self._username = username
       self._password = password
       self.admin = admin
       self.borrowedBooks = []

    def loginProcess(self):
        print(f"{self._username} ha iniciado sesion exitosamente, Bienvenido {self._name}!")

    def borrowBook(self,book:Book):
        if len(self.borrowedBooks) >= 3:
            print("You can't borrow more than 3 books, Sorry! Business rules")
            return
        
        if book.isBorrowed:
            print(f"{book.title} is already borrowed by someone else, try again tomorrow buddy!")
            return

        self.borrowedBooks.append(book)
        book.isBorrowed = True
        print(f"{self._name} borrowed {book.title} successfully!")
       
    def returnBook(self,book:Book):
        if book in self.borrowedBooks:
            book.isBorrowed = False
            self.borrowedBooks.remove(book)
            print(f"{self._name} returned : {book.title} successfully!")
        else: 
            print(f"Book hasn't borrowed")

    def showBorrowedBooks(self):
        if not self.borrowedBooks:
            print(f"{self._name} has no borrowed any books.")
        else:
            print(f"Books borrowed by {self._name}:")
            for book in self.borrowedBooks:
                print(f"- {book.title} by {book.author} - {"Borrowed" if book.isBorrowed else "Available"}")

    def showAllBooks(self):
        print("All our books:")
        for book in self.admin.catalog:
            print(book.description())

    def logOutProcess(self):
         print(f"{self._username} has logged out, See you later!")
     