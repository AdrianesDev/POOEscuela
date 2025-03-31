from Book import Book
from User import User
from Library import Library
from RoleProtocol import RoleProtocol
from Admin import Admin
from Invitado import Invitado


admin = Admin("Adrian Catañeda", "Adrian456", "1548")
invitado = Invitado("Invitado4", admin)
user = User("Marco Oregel", "Jz4", "1234", admin)


Book1 = Book("1984", "George Orwell" )
Book2 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez")
Book3 = Book("The little Prince", "Antoine de Saint-Exupery")
Book4 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
Book5 = Book("Fahrenheit 451", "Bradbury")
Book6 = Book("Harry Potter", "J.K Rowling")

admin.loginProcess()
print("-" * 65)
admin.addBook(Book1)
admin.addBook(Book2)
admin.addBook(Book3)
admin.addBook(Book4)
admin.addBook(Book5)
admin.addBook(Book6)
print("-" * 65)
admin.removeBook(Book6)
print("-" * 65)

admin.showAllBooks()
print("-" * 65)
admin.showAvailableBooks()
print("-" * 65)
admin.findBook("1984")
print("-" * 65)

admin.logOutProcess()
print("-" * 65)

invitado.loginProcess()
print("-" * 65)

user.loginProcess()
user.borrowBook(Book1)
user.borrowBook(Book2)
user.borrowBook(Book3)
user.borrowBook(Book4)
print("-" * 65)

user.showBorrowedBooks()
print("-" * 65)

user.showAllBooks()
print("-" * 65)

user.returnBook(Book1)
print("-" * 65)
user.showBorrowedBooks()
print("-" * 65)
user.borrowBook(Book5)
print("-" * 65)
user.showAllBooks()
print("-" * 65)
user.logOutProcess()
print("-" * 65)

user.addBook(Book2)



