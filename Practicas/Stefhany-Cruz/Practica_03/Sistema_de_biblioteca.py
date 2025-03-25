class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.isBorrowed = False 

    def description(self) -> str:
        return f"'{self.title}' por {self.author}"

class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowedBooks: list[Book] = []

    def borrowBook(self, book: Book):
        if len(self.borrowedBooks) >= 3:
            print(f"{self.name} alcanzo el límite de libros.")
            return
        if book.isBorrowed:
            print(f"El libro '{book.title}' está prestado.")
            return
        book.isBorrowed = True
        self.borrowedBooks.append(book)
        print(f"{self.name} ha tomado prestado: {book.description()}")

    def returnBook(self, book: Book):
        if book in self.borrowedBooks:
            book.isBorrowed = False
            self.borrowedBooks.remove(book)
            print(f"\n {self.name} ha devuelto: {book.description()}")
        else:
            print(f"{self.name} no tiene el libro '{book.title}' prestado.")

class Library:
    def __init__(self):
        self.catalog: list[Book] = []

    def addBook(self, book: Book):
        self.catalog.append(book)
        print(f"Libro agregado al catálogo: {book.description()}")

    def findBook(self, title: str) -> Book | None:
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        print(f"No se encontró el libro con título '{title}'")
        return None

    def showAvailableBooks(self):
        disponibles = [book for book in self.catalog if not book.isBorrowed]
        if not disponibles:
            print("No hay libros disponibles actualmente.")
        else:
            print("\n Libros disponibles:")
            for book in disponibles:
                print(f"- {book.description()}")

library = Library()
book1 = Book("La paciente silenciosa", "Alex Michaelides")
book2 = Book("El jardin de las mariposas", "Dot Hutchison")
book3 = Book("Invisible", "Eloy Moreno")
book4 = Book("Tu mentira más dulce", "Maria Goodin")

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)
library.addBook(book4)

user = User("Stefhany Cruz")

user.borrowBook(book1)
user.borrowBook(book2)
user.borrowBook(book3)
user.borrowBook(book4)  

library.showAvailableBooks()

user.returnBook(book2)

library.showAvailableBooks()