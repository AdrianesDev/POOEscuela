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
    def __init__(self, Name):
        self.name = Name
        self.BorrowedBooks = []

    def Borrowed_Book(self, Book):
        if not Book.isBorrowed:
            Book.isBorrowed = True
            self.BorrowedBooks.append(Book)
            print(f"{self.name} tomo prestado: {book.title}")
        else:
            print(f"El libro {book.title} ya esta prestado.")

    def Return_Book(self, Book):
        if Book in self.BorrowedBooks:
            Book.isBorrowed = False
            self.BorrowedBooks.remove(Book)
            print(f"{self.name} devolvio: {book.title}")
        else:
            print(f"El libro {self.name} no exite ese libro.")

class Library:
    def __init__(self):
        self.catalog = []

    def addBorrowed(self, Book):
        if Book not in self.catalog:
            self.catalog.append(Book)
            print(f"Se agrego {book.title} al catalogo.")
        else:
            print(f"El libro {book.title} ya esta en el catalogo.")

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
                print(f" - {book.title}")

library = Library()
books = [
    Book("1984", "George Orwell"),
    Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez"),
    Book("The Little Prince", "Antoine de Saint-Exupery"),
    Book("Fahrenheit 451", "Ray Bradbury"),
    Book("Harry Potter", "J.K Rowling"),
]


for book in books:
    library.addBorrowed(book)  

print("-" * 10)

user = User("Adrian")

print("-" * 10)

user.Borrowed_Book(library.findBook("1984"))  
user.Borrowed_Book(library.findBook("One Hundred Years of Solitude"))
user.Borrowed_Book(library.findBook("The Little Prince"))

print([book.title for book in user.BorrowedBooks])

print("-" * 10)

library.ShowAvailableBook()  

user.Return_Book(library.findBook("One Hundred Years of Solitude"))  
user.Borrowed_Book(library.findBook("Fahrenheit 451"))

print([book.title for book in user.BorrowedBooks])

print("-" * 10)

library.ShowAvailableBook()