class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def description(self):
        return f"'{self.title}' de {self.author} - {'Prestado' if self.is_borrowed else 'Disponible'}"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} no puede pedir más de 3 libros prestados.")
            return
        
        if book.is_borrowed:
            print(f"El libro '{book.title}' ya está prestado.")
            return
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} ha tomado prestado '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto '{book.title}'.")
        else:
            print(f"{self.name} no tiene el libro '{book.title}' prestado.")

    def list_borrowed_books(self):
        print(f"Libros prestados por {self.name}:")
        for book in self.borrowed_books:
            print(f"- {book.description()}")
        print()


class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
        print(f"El libro '{book.title}' ha sido añadido a la biblioteca.")

    def find_book(self, title):
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_available_books(self):
        available_books = [book for book in self.catalog if not book.is_borrowed]
        if not available_books:
            print("No hay libros disponibles en este momento.")
        else:
            print("Libros disponibles:")
            for book in available_books:
                print(f"- {book.description()}")


library = Library()
books = [
    Book("1984", "George Orwell"),
    Book("Cien años de soledad", "Gabriel García Márquez"),
    Book("El principito", "Antoine de Saint-Exupéry"),
    Book("Fahrenheit 451", "Ray Bradbury"),
    Book("Harry Potter", "J.K. Rowling"),
]

for book in books:
    library.add_book(book)

user = User("Adrián")

user.borrow_book(library.find_book("1984"))
user.borrow_book(library.find_book("Cien años de soledad"))
user.borrow_book(library.find_book("El principito"))
user.list_borrowed_books()
library.show_available_books()
user.return_book(library.find_book("Cien años de soledad"))
user.borrow_book(library.find_book("Fahrenheit 451"))
user.list_borrowed_books()
library.show_available_books()
