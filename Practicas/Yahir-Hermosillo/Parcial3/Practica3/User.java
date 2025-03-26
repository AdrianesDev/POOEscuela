import java.util.ArrayList;
import java.util.List;

public class User {
    private String name;
    private List<Book> borrowedBooks;
    
    public User(String name) {
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }
    
    public String getName() {
        return name;
    }
    
    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }
    
    public void borrowBook(Book book) {
        if(book == null) return;
        
        if(borrowedBooks.size() >= 3) {
            System.out.println(name + " cannot borrow more than 3 books!");
            return;
        }
        
        if(book.isBorrowed()) {
            System.out.println("'" + book.getTitle() + "' is already borrowed!");
            return;
        }
        
        book.setBorrowed(true);
        borrowedBooks.add(book);
        System.out.println(name + " borrowed '" + book.getTitle() + "'");
    }
    
    public void returnBook(Book book) {
        if(book == null) return;
        
        if(borrowedBooks.remove(book)) {
            book.setBorrowed(false);
            System.out.println(name + " returned '" + book.getTitle() + "'");
        }
    }
}
