from enum import Enum

class Role(Enum):
    ADMIN = "Admin"
    USER = "User"
    GUEST = "Guest"

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def description(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class User:
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.borrowed_books = []
    
    def borrow_book(self, book: Book) -> bool:
        if self.role == Role.GUEST:
            print("The Guest can't borrowed books.")
            return False
        
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} has 3 books already, you can't take more.")
            return False
        
        if book.is_borrowed:
            print(f"'{book.title}' is borrowed.")
            return False
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} has borrowed '{book.title}'")
        return True
    
    def return_book(self, book: Book) -> bool:
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        else:
            print(f"{self.name} doesn't have '{book.title}'")
            return False
    
    def show_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} doesn't have borrowed books.")
        else:
            print(f"Borrowed books to {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.description()}")

class Library:
    def __init__(self):
        self.catalog = []
    
    def add_book(self, book: Book, user: User) -> bool:
        if user.role != Role.ADMIN:
            print("Only the admins can be add books.")
            return False
        
        self.catalog.append(book)
        print(f"The book '{book.title}' add in the catalog.")
        return True
    
    def remove_book(self, book: Book, user: User) -> bool:
        if user.role != Role.ADMIN:
            print("Only the admins can delete books.")
            return False
        
        if book in self.catalog:
            if book.is_borrowed:
                print(f"Can't been remove '{book.title}' because is borrowed.")
                return False
            self.catalog.remove(book)
            print(f"The book '{book.title}' remove to the catalog.")
            return True
        else:
            print(f"The book '{book.title}' isn't in the catalog.")
            return False
    
    def find_book(self, title: str) -> Book:
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def show_available_books(self):
        available_books = [book for book in self.catalog if not book.is_borrowed]
        if not available_books:
            print("There no have books here.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.description()}")

if __name__ == "__main__":

    library = Library()

    admin = User("Admin Principal", Role.ADMIN)
    user1 = User("Juan Pérez", Role.USER)
    guest = User("Invitado", Role.GUEST)

    book1 = Book("Chavo del ocho", "Roberto Gómez Bolaños")
    book2 = Book("1984", "George Orwell")
    book3 = Book("El Principito", "Antoine de Saint-Exupéry")
    book4 = Book("Don Quijote", "Miguel de Cervantes")
    
    library.add_book(book1, admin)
    library.add_book(book2, admin)
    library.add_book(book3, admin)
    library.add_book(book4, admin)
    
    print("\n Initial status ")
    library.show_available_books()
    user1.show_borrowed_books()
    
    book5 = Book("Luna de pluton", "Dross")
    library.add_book(book5, user1)
 
    print("\n Borrowed ")
    user1.borrow_book(book1)
    user1.borrow_book(book2)
    user1.borrow_book(book3)

    user1.borrow_book(book4)

    print("\n Last Borrowed ")
    library.show_available_books()
    user1.show_borrowed_books()

    print("\n Test Guest ")
    guest.borrow_book(book4)
    library.show_available_books()

    print("\nReturned ")
    user1.return_book(book2)
    
    library.show_available_books()
    user1.show_borrowed_books()

    print("\n Remove Books ")
    library.remove_book(book1, admin)

    library.remove_book(book4, admin)