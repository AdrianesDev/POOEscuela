class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isBorrowed = False

    def description(self) -> str:
        status = "Available" if not self.isBorrowed else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"
    
class Person:
    def __init__(self, name: str):
        self.name: str = name

class User(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.borrowedBooks: list[Book] = []

    def borrowBook(self, book: Book) -> bool:
        if len(self.borrowedBooks) >= 3:
            print(f"{self.name} cannot borrow more than 3 books.")
            return False
        
        if book.isBorrowed:
            print(f"The Book '{book.title}' is already borrowed.")
            return False
        
        book.isBorrowed = True
        self.borrowedBooks.append(book)
        print(f"{self.name} has borrowed '{book.title}'")
        return True
    
    def returnBook(self, book: Book) -> bool:
        if book not in self.borrowedBooks:
            print(f"{self.name} has not borrowed '{book.title}'")
            return False
        
        book.isBorrowed = False
        self.borrowedBooks.remove(book)
        print(f"{self.name} has returned '{book.title}'")
        return True

class Admin(Person):
    def addBook(self, library, book: Book):
        library.addBook(book)

    def removeBook(self, library, book: Book):
        library.removeBook(book)

class Guest(Person):
    def viewAvailableBooks(self, library):
        return library.showAvailableBooks()            

class Library:
    def __init__(self):
        self.catalog: list[Book] = []

    def addBook(self, book: Book):
        self.catalog.append(book)
        print(f"Book added: {book.title}")

    def removeBook(self, book: Book):
        if book in self.catalog:
            self.catalog.remove(book)
            print(f"Book removed: {book.title}")
        else:
            print("Book not found in catalog")

    def findBook(self, title: str) -> Book | None:
        for book in self.catalog:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def showAvailableBooks(self) -> list[Book]:
        available_books = [book for book in self.catalog if not book.isBorrowed]

        if not available_books:
            print("No books are currently available.")
            return []
        
        for book in available_books:
            print(book.description())

        return available_books

def main():
    # Create a separator line
    def print_separator():
        print("-" * 50)

    library = Library()

    book1 = Book("1984","George Orwell")
    book2 = Book("One Hundred Years of Solitude","Gabriel García Márquez")
    book3 = Book("The Little Prince","Antoine de Saint-Exupéry")
    book4 = Book("Fahrenheit 451","Ray Bradbury")
    book5 = Book("Harry Potter","J.K. Rowling")

    admin = Admin("Juan")

    admin.addBook(library, book1)
    admin.addBook(library, book2)
    admin.addBook(library, book3)
    admin.addBook(library, book4)
    admin.addBook(library, book5)

    user = User("Adrian")

    print("Books borrowed by Adrian:")
    user.borrowBook(book1)
    user.borrowBook(book2)
    user.borrowBook(book3)

    print_separator()
    print("Available books:")
    library.showAvailableBooks()

    print_separator()
    user.returnBook(book2)
    user.borrowBook(book4)

    print("Books borrowed by Adrian:")
    print("\n".join([book.description() for book in user.borrowedBooks]))

    print_separator()
    print("Available books:")
    library.showAvailableBooks()

if __name__ == "__main__":
    main()