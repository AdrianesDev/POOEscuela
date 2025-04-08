from Book import Book
from User import User
from Library import Library

user = User("Marco Oregel")

Book1 = Book("1984", "George Orwell" )
Book2 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez")
Book3 = Book("The little Prince", "Antoine de Saint-Exupery")
Book4 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
Book5 = Book("Fahrenheit 451", "Bradbury")
Book6 = Book("Harry Potter", "J.K Rowling")

library = Library()
library.addBook(Book1)
library.addBook(Book2)
library.addBook(Book3)
library.addBook(Book4)
library.addBook(Book5)
library.addBook(Book6)

print("-" * 65)
user.borrowBook(Book1)
user.borrowBook(Book2)
user.borrowBook(Book3)
user.borrowBook(Book4)
print("-" * 65)

user.showBorrowedBooks()
print("-" * 65)

library.showAvailableBooks()
print("-" * 65)

user.returnBook(Book1)
print("-" * 65)

user.borrowBook(Book5)
print("-" * 65)

user.showBorrowedBooks()
print("-" * 65)

library.showAvailableBooks()
print("-" * 65)

library.showAllBooks()
print("-" * 65)







