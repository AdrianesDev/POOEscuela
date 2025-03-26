class Book: 
    def __init__(self , Title, Author):
        self.title = Title
        self.author = Author
        self.isBorrowed = False

    def Lend(self):
        if not self.isBorrowed:
            self.isBorrewed = True
            print(f"El libro {self.title} ha sido prestado.")
        else:
            print(f"El libro {self.title} no ha sido prestado.")
        
    def Return(self):    
        if self.isBorrowed:
            self.isBorrowed = False
            print(f"El libro {self.title} ha sido devuelto.")
        else: 
            print(f"El libro {self.title} no ha sido devuelto.")

class User:
    def __init__(self, Name, Role):
        self.name = Name
        self.role = Role
        self.BorrowedBooks = []

    def CanBorrowed(self):
        return self.role in ["Admin", "User"]
    
    def CanManageBooks(self):
        return self.role == "Admin"

    def BorrowedBook(self, book):
        if not self.CanBorrowed():
            print(f"ERROR: Los usuarios {self.role} no pueden tomar libros prestados.")
            return
        
        if not book.isBorrowed:
            book.Lend()
            self.BorrowedBooks.append(book)
            print(f"{self.name} tomo prestado: {book.title}")
        else: 
            print(f"El libro {book.title} ya esta prestado.")

    def ReturnBook(self, book):
        if book in self.BorrowedBooks:
            book.ReturnBook()
            self.BorrowedBooks.remove(book)
            print(f"{self.name} devolvio: {book.title}")
        else:
            print(f"ERROR: {self.name} no tiene prestado el libro {book.title}")

class Admin(User):
    def __init__(self, name):
        super().__init__(name, "Admin")

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name, "User")

class Guest(User):
    def __init__(self, name):
        super().__init__(self, "Guest")

    def BorrowedBook(self, book):
        print(f"ERROR: Los invitados no pueden tomar libros prestados.")

class Library:
    def __init__(self):
        self.catalog = []

    def addBorrowed(self, user, book):
        if not user.CanManageBooks():
            print(f"ERROR: Solo los administradores pueden agregar libros.")
            return
        
        if book not in self.catalog:
            self.catalog.append(book) 
            print(f"Se agrego {book.title}")
        else:
            print(f"El libro {book.title} ya esta en el catalogo.")

    def RemoveBook(self, user, book):
        if not user.CanManageBooks():
            print(f"ERROR: Solo los administradores pueden eliminar libros del catalogo.")
            return
        
        if book in self.catalog:
            self.catalog.remove(book)
            print(f"Se elimino {book.title} del catalogo.")
        else: 
            print(f"El libro {book.title} no exite en el catalogo.")

    def findBook(self, Title):
        for book in self.catalog:
            if book.title.lower() == Title.lower():
                return book
        return None
        
    def ShowAvailableBook(self):
        available = [book for book in self.catalog if not book.isBorrowed]

        if not available:
            print("No hay libros disponibles.")
        else: 
            print("Libros disponible: ")
            for book in available:
                print(f" - {book.title} por {book.author}")

library = Library()

admin = Admin("Adrian")
user = RegularUser("Elit")
guest = Guest("Juan")

books = [
    Book("1984", "George Orwell"),
    Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
    Book("The Little Prince", "Antoine de Saint-Exupery"),
    Book("Fahrenheit 451", "Ray Bradbury"),
    Book("Harry Potter", "J.K Rowling"),
]

print("\nAdmin agregando libros: ")
for book in books:
    library.addBorrowed(admin, book)  

print("\nUsuario regular intentando agregar libro:")
new_book = Book("Fahrenheit 451", "Ray Bradbury")
library.addBorrowed(user, book)

print("\nAdmin agregando un libro: ")
library.addBorrowed(admin, book)

print("\nLibros disponibles en la biblioteca: ")
library.ShowAvailableBook()

print("\nUsuario regular tomo prestado un libro: ")
user.BorrowedBook(library.findBook("1984"))

print("\nInvitado intentando tomar prestado un libro: ")
user.BorrowedBook(library.findBook("The Little Prince"))

print("\nLibros disponibles despues de prestamos: ")
library.ShowAvailableBook()

print("\nAdmin eliminando un libro: ")
library.RemoveBook(admin, library.findBook("One Hundred Years of Solitude"))

print("\nEstado final de los libros disponibles: ")
library.ShowAvailableBook()