import Foundation

class Book {
    let title: String
    let author: String
    var isBorrowed: Bool = false
    
    init(title: String, author: String) {
        self.title = title
        self.author = author
    }
    
    func description() -> String {
        return "‘\(title)’ by \(author) - \(isBorrowed ? "Borrowed" : "Available")"
    }
}

class User {
    let name: String
    var borrowedBooks: [Book] = []
    
    init(name: String) {
        self.name = name
    }
    
    func borrowBook(_ book: Book) {
        if borrowedBooks.count >= 3 {
            print("\(name) already has 3 borrowed books. Cannot borrow more.")
            return
        }
        
        if book.isBorrowed {
            print("The book ‘\(book.title)’ is already borrowed.")
            return
        }
        
        book.isBorrowed = true
        borrowedBooks.append(book)
        print("\(name) borrowed ‘\(book.title)’")
    }
    
    func returnBook(_ book: Book) {
        if let index = borrowedBooks.firstIndex(where: { $0 === book }) {
            borrowedBooks.remove(at: index)
            book.isBorrowed = false
            print("\(name) returned ‘\(book.title)’")
        } else {
            print("\(name) doesn't have the book ‘\(book.title)’")
        }
    }
    
    func showBorrowedBooks() {
        print("\nBooks borrowed by \(name):")
        if borrowedBooks.isEmpty {
            print("- None")
        } else {
            for book in borrowedBooks {
                print("- \(book.description())")
            }
        }
    }
}

class Library {
    var catalog: [Book] = []
    
    func addBook(_ book: Book) {
        catalog.append(book)
    }
    
    func findBook(byTitle title: String) -> Book? {
        return catalog.first(where: { $0.title.lowercased() == title.lowercased() })
    }
    
    func showAvailableBooks() {
        print("\nAvailable books:")
        let available = catalog.filter { !$0.isBorrowed }
        if available.isEmpty {
            print("- No books available at the moment.")
        } else {
            for book in available {
                print("- \(book.description())")
            }
        }
    }
}


// Create library and books
let library = Library()

let book1 = Book(title: "1984", author: "George Orwell")
let book2 = Book(title: "One Hundred Years of Solitude", author: "Gabriel García Márquez")
let book3 = Book(title: "The Little Prince", author: "Antoine de Saint-Exupéry")
let book4 = Book(title: "Fahrenheit 451", author: "Ray Bradbury")
let book5 = Book(title: "Harry Potter", author: "J.K. Rowling")

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)
library.addBook(book4)
library.addBook(book5)

// Create a user
let user = User(name: "Adrian")

// Borrow up to 3 books
user.borrowBook(book1)
user.borrowBook(book2)
user.borrowBook(book3)

// Try to borrow a 4th book (should fail)
user.borrowBook(book4)

// Show borrowed books
user.showBorrowedBooks()

// Show available books
library.showAvailableBooks()

// Return a book
user.returnBook(book2)

// Try borrowing again (should now succeed)
user.borrowBook(book4)

// Show updated status
user.showBorrowedBooks()
library.showAvailableBooks()
