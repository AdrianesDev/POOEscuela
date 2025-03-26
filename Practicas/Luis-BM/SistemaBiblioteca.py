class Book:
    def __init__(self, title: str, author: str, is_borrowed: bool = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed 

    def description(self) -> str:
        status = "Prestado" if self.is_borrowed else "Disponible"
        return f"{self.title} by {self.author} - {status}"

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.borrowed_books = []

    def borrow_book(self, book):
        if self.role == "Invitado":
            print("El invitado no puede prestar libros")
            return
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} no se puede prestar mas de 3 libros")
            return
        if book.is_borrowed:
            print(f"{book.title} ya esta prestado")
            return
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} tiene prestado {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto {book.title}.")
        else:
            print(f"{self.name} no tiene {book.title}.")

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book, user):
        if user.role != "Admin":
            print(f"Solo el Admin puede agragar libros")
            return
        self.catalog.append(book)
        print(f"{book.title} Añadido al catalogo")

    def find_book(self, title):
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        return None

    def show_available_books(self):
        available_books = [book for book in self.catalog if not book.is_borrowed]
        if available_books:
            print("Libros disponibles:")
            for book in available_books:
                print(book.description())  
        else:
            print("No hay libros disponibles")

library = Library()

admin = User("Adrian", "Admin")
user = User("Luis BM", "User")
guest = User("Juan", "Guest")

library.add_book(Book("Maravilloso desastre", "Jamie McGuire"), admin)
library.add_book(Book("Cuando no queden más estrellas que contar", "Maria Martinez"), admin)
library.add_book(Book("Tu y otros desastres naturales", "Maria Martinez"), admin)
library.add_book(Book("La fragilidad de un corazón bajo la lluvia", "Maria Martinez"), admin)

library.show_available_books()

user.borrow_book(library.catalog[0])  
user.borrow_book(library.catalog[1]) 
user.borrow_book(library.catalog[2])  
user.borrow_book(library.catalog[3])

library.show_available_books()

user.return_book(library.catalog[0])  
library.show_available_books()

guest.borrow_book(library.catalog[1])  
