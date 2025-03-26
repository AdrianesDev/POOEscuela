class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def description(self, role):
        if role in ("admin", "user"):
            return f"'{self.title}' de {self.author} - {'Prestado' if self.is_borrowed else 'Disponible'}"
        elif role == "invitado":
            return "Los invitados no pueden ver el estado de los libros."
        else:
            return "Rol no válido."

class User:
    def __init__(self, name, role):
        if role not in ("admin", "user", "invitado"):
            raise ValueError("Rol no válido. Use 'admin', 'user' o 'invitado'.")
        
        self.name = name
        self.role = role
        self.borrowed_books = []

    def borrow_book(self, book):
        if self.role == "invitado":
            print(f"{self.name} no tiene permiso para pedir libros prestados.")
            return
        
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
            print(f"- {book.description(self.role)}")
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

    def show_available_books(self, role):
        if role == "invitado":
            print("Los invitados solo pueden ver los títulos de los libros.")
            for book in self.catalog:
                print(f"- {book.title}")
        else:
            available_books = [book for book in self.catalog if not book.is_borrowed]
            if not available_books:
                print("No hay libros disponibles en este momento.")
            else:
                print("Libros disponibles:")
                for book in available_books:
                    print(f"- {book.description(role)}")

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

admin = User("Carlos", "admin")
usuario = User("Adrián", "user")
invitado = User("María", "invitado")

usuario.borrow_book(library.find_book("1984"))
usuario.borrow_book(library.find_book("Cien años de soledad"))
usuario.borrow_book(library.find_book("El principito"))

usuario.list_borrowed_books()
library.show_available_books(usuario.role)

usuario.return_book(library.find_book("Cien años de soledad"))
usuario.borrow_book(library.find_book("Fahrenheit 451"))

usuario.list_borrowed_books()
library.show_available_books(usuario.role)

invitado.borrow_book(library.find_book("1984"))
library.show_available_books(invitado.role)