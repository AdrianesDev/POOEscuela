from Book import Book
from Library import Library
class User:

    def __init__(self,name):
        self.name = name
        self.borrowedBooks = []

    def borrowBook(self,book:Book):
        if len(self.borrowedBooks) >= 3:
            print("You can't borrow more than 3 books, Sorry! Business rules")
            return
        
        if book.isBorrowed:
            print(f"{book.title} is already borrowed by someone else, try again tomorrow buddy!")
            return

        self.borrowedBooks.append(book)
        book.isBorrowed = True
        print(f"{self.name} borrowed {book.title} successfully!")
       
    def returnBook(self,book:Book):
        if book in self.borrowedBooks:
            book.isBorrowed = False
            self.borrowedBooks.remove(book)
            print(f"{self.name} returned : {book.title} successfully!")
        else: 
            print(f"Book hasn't borrowed")

    def showBorrowedBooks(self):
        if not self.borrowedBooks:
            print(f"{self.name} has no borrowed any books.")
        else:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowedBooks:
                print(f"- {book.title} by {book.author} - {"Borrowed" if book.isBorrowed else "Available"}")
     