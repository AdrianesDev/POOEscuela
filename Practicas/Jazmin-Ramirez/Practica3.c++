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

class Library {
public:
    vector<Book> catalog;

    void addBook(const Book &book) {
        catalog.push_back(book);
    }

    Book* findBook(const string &title) {
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

    void removeBook(const string &title) {
        for (size_t i = 0; i < catalog.size(); i++) {
            if (catalog[i].title == title) {
                if (catalog[i].isBorrowed) {
                    cout << "No se puede eliminar '" << title << "' porque está prestado.\n";
                    return;
                }
                catalog.erase(catalog.begin() + i);
                cout << "El libro '" << title << "' ha sido eliminado del catálogo.\n";
                return;
            }
        }
        cout << "El libro '" << title << "' no fue encontrado en el catálogo.\n";
    }
};

class User {
public:
    string name;
    virtual string getRole() { return "Usuario"; }
    vector<Book*> borrowedBooks;

    User(string n) : name(n) {}

    virtual void borrowBook(Book* book) {
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

    virtual void returnBook(Book* book) {
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

    virtual void addBook(Library &library, const Book &book) {
        cout << "Solo un administrador puede agregar libros al catálogo.\n";
    }
};

class Admin : public User {
public:
    Admin(string n) : User(n) {}
    string getRole() override { return "Admin"; }

    void addBook(Library &library, const Book &book) override {
        library.addBook(book);
        cout << "El administrador ha agregado el libro '" << book.title << "'.\n";
    }

    void removeBook(Library &library, const string &title) {
        library.removeBook(title);
    }
};

class Guest : public User {
public:
    Guest(string n) : User(n) {}
    string getRole() override { return "Invitado"; }

    void borrowBook(Book* book) override {
        cout << "Los invitados no pueden pedir prestados libros.\n";
    }
    void returnBook(Book* book) override {
        cout << "Los invitados no pueden devolver libros.\n";
    }
};

int main() {
    Library library;
    library.addBook(Book("Termina Conmigo", "Colleen Hoover"));
    library.addBook(Book("La Hipótesis del Amor", "Ali Hazelwood"));
    library.addBook(Book("Lectura en la Playa", "Emily Henry"));

    Admin admin("Carlos");
    User user("Jazmin");
    Guest guest("Luis");

    library.showAvailableBooks();

    Book* book1 = library.findBook("La Hipótesis del Amor");
    if (book1) user.borrowBook(book1);

    Book* book2 = library.findBook("Lectura en la Playa");
    if (book2) guest.borrowBook(book2); 

    library.showAvailableBooks();

    admin.addBook(library, Book("Boulevard", "Flor M. Salvador"));
   
    admin.removeBook(library, "Termina Conmigo");

    user.returnBook(book1);

    library.showAvailableBooks();
    
    admin.addBook(library, Book("sinestesia", "Cas Alvarez"));
    
    admin.addBook(library, Book("Barroco", "Cas Alvarez"));
    
    admin.addBook(library, Book("Anestecia", "Cas Alvarez"));
    
    admin.addBook(library, Book("Espinas", "Cas Alvarez"));
    
    admin.addBook(library, Book("Fuego", "Cas Alvarez"));
    
    admin.addBook(library, Book("Morfina", "Cas Alvarez"));
    
    user.addBook(library, Book("Ecuacion", "Cas Alvarez"));
    
    guest.borrowBook(library.findBook("Boulevard"));
    return 0;
};
