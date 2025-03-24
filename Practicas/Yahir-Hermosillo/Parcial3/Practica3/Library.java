import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<Book> catalog;
    
    public Library() {
        this.catalog = new ArrayList<>();
    }
    
    public void addBook(Book book) {
        catalog.add(book);
    }
    
    public Book findBook(String title) {
        for(Book book : catalog) {
            if(book.getTitle().equals(title)) {
                return book;
            }
        }
        return null;
    }
    
    public void showAvailableBooks() {
        for(Book book : catalog) {
            if(!book.isBorrowed()) {
                System.out.println("- '" + book.getTitle() + "' by " + book.getAuthor() + " - " + book.getStatus());
            }
        }
    }
}