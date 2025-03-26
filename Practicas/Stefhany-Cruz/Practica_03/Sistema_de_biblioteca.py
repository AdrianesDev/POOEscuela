class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.isBorrowed = False 

    def description(self) -> str:
        return f"'{self.title}' por {self.author}"

class Person:
    def __init__(self, name: str):
        self.name = name

class User(Person):
    def __init__(self, name: str):
        super().__init__(name)
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

class Admin(User):
    def __init__(self, name: str):
        super().__init__(name)

    def addBookToLibrary(self, library, book: Book):
        library._addBook(book)
        print(f"{self.name} agregó el libro: {book.description()}")

    def removeBookFromLibrary(self, library, title: str):
        book = library.findBook(title)
        if book:
            if book.isBorrowed:
                print(f"No se puede eliminar el libro '{title}' porque está prestado.")
            else:
                library._removeBook(book)
                print(f"{self.name} eliminó el libro: {book.description()}")
        else:
            print(f"No se encontró el libro '{title}' para eliminar.")

class Guest(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def borrowBook(self, book: Book):
        print(f"{self.name} inicia sesión para tomar libros prestados.")

    def returnBook(self, book: Book):
        print(f"{self.name} no hay libros para devolver.")

class Library:
    def __init__(self):
        self.catalog: list[Book] = []

    def _addBook(self, book: Book):
        self.catalog.append(book)
        
    def _removeBook(self, book: Book):
        self.catalog.remove(book)

    def findBook(self, title: str) -> Book | None:
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book       
        return None

    def showAvailableBooks(self):
        disponibles = [book for book in self.catalog if not book.isBorrowed]
        if not disponibles:
            print("No hay libros disponibles actualmente.")
        else:
            print("\n Libros disponibles:")
            for book in disponibles:
                print(f"- {book.description()}")

biblioteca = Library()

# Crear personas con distintos roles
admin = Admin("Wendy Lopez")
usuario = User("Stefhany Cruz")
invitado = Guest("Veronica Garibaldi")

# Admin agrega libros
admin.addBookToLibrary(biblioteca, Book("La paciente silenciosa", "Alex Michaelides"))
admin.addBookToLibrary(biblioteca, Book("El jardin de las mariposas", "Dot Hutchison"))
admin.addBookToLibrary(biblioteca, Book("Tu mentira más dulce", "Maria Goodin"))

# Todos ven los libros disponibles
biblioteca.showAvailableBooks()

# Usuario toma un libro
libro = biblioteca.findBook("El jardin de las mariposas")
if libro:
    usuario.borrowBook(libro)

# Invitado intenta tomar un libro
libro2 = biblioteca.findBook("Tu mentira más dulce")
if libro2:
    invitado.borrowBook(libro2)

# Admin intenta eliminar un libro prestado
admin.removeBookFromLibrary(biblioteca, "El jardin de las mariposas")

# Usuario devuelve el libro
usuario.returnBook(libro)

# Admin elimina el libro
admin.removeBookFromLibrary(biblioteca, "El jardin de las mariposas")