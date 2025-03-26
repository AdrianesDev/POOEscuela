#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Book {
public:
    string title;
    string author;
    bool isBorrowed;

    Book(string t, string a) : title(t), author(a), isBorrowed(false) {}

    string description() {
        return title + " de " + author + (isBorrowed ? " (Prestado)" : " (Disponible)");
    }
};

class User {
public:
    string name;
    vector<Book*> borrowedBooks;

    User(string n) : name(n) {}

    void borrowBook(Book* book) {
        if (borrowedBooks.size() >= 3) {
            cout << name << " no puede pedir prestados más de 3 libros.\n";
            return;
        }
        if (book->isBorrowed) {
            cout << "El libro '" << book->title << "' ya está prestado.\n";
            return;
        }
        book->isBorrowed = true;
        borrowedBooks.push_back(book);
        cout << name << " ha tomado prestado '" << book->title << "'.\n";
    }

    void returnBook(Book* book) {
        for (size_t i = 0; i < borrowedBooks.size(); i++) {
            if (borrowedBooks[i] == book) {
                book->isBorrowed = false;
                borrowedBooks.erase(borrowedBooks.begin() + i);
                cout << name << " ha devuelto '" << book->title << "'.\n";
                return;
            }
        }
        cout << "El libro '" << book->title << "' no fue prestado por " << name << ".\n";
    }
};

class Library {
public:
    vector<Book> catalog;

    void addBook(Book book) {
        catalog.push_back(book);
    }

    Book* findBook(string title) {
        for (Book &book : catalog) {
            if (book.title == title) {
                return &book;
            }
        }
        return nullptr;
    }

    void showAvailableBooks() {
        cout << "\nLibros disponibles en la biblioteca:\n";
        for (Book &book : catalog) {
            if (!book.isBorrowed) {
                cout << " - " << book.description() << "\n";
            }
        }
    }
};

int main() {
    Library library;
    library.addBook(Book("Termina Conmigo", "Colleen Hoover"));
    library.addBook(Book("La Hipótesis del Amor", "Ali Hazelwood"));
    library.addBook(Book("Lectura en la Playa", "Emily Henry"));
    
    User user("Jazmin");
    
    library.showAvailableBooks();
    
    Book* book1 = library.findBook("La Hipótesis del Amor");
    if (book1) user.borrowBook(book1);
    
    Book* book2 = library.findBook("Lectura en la Playa");
    if (book2) user.borrowBook(book2);
    
    library.showAvailableBooks();
    
    user.returnBook(book1);
    
    library.showAvailableBooks();
    
    return 0;
}
