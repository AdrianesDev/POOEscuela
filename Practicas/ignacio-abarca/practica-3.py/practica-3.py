class Book:
    def __init__(self, title, author, isBorrowed):

        self.title = title
        self.author = author
        self.isBorrowed = isBorrowed
    def description(self):
        return f"Titulo: {self.title}, Autor: {self.author}, Prestado: {'Sí' if self.isBorrowed else 'No'}"

class User:
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []

    def borrowBook(self, book):
        if len(self.borrowedBooks) >= 3:
            print(f"{self.name} ya tiene 3 libros prestados. No puede pedir más.")
            return
        
        if book.isBorrowed:
            print(f"El libro '{book.title}' ya está prestado.")
            return
        
        book.isBorrowed = True
        self.borrowedBooks.append(book)
        print(f"{self.name} ha tomado prestado '{book.title}'.")

    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.isBorrowed = False
            self.borrowedBooks.remove(book)
            print(f"{self.name} ha devuelto '{book.title}'.")
        else:
            print(f"{self.name} no tiene el libro '{book.title}' prestado.")

class Library:
    def __init__(self):
        self.catalog = []

    def addBook(self, book):
        self.catalog.append(book)
        print(f"El libro '{book.title}' ha sido anadido a la biblioteca.")

    def findBook(self, title):
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        return None

    def showAvailableBooks(self):
        available_books = [book for book in self.catalog if not book.isBorrowed]
        if not available_books:
            print("No hay libros disponibles en este momento.")
        else:
            print("Libros disponibles:")
            for book in available_books:
                print(f"- {book.title} de {book.author}")