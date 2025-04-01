// Library.java
import java.util.ArrayList;

public class Library {
    private ArrayList<Book> catalog;
    
    public Library() {
        this.catalog = new ArrayList<>();
    }
    
    public void addBook(Book book, User user) {
        if (user.getRole() instanceof Admin) {
            catalog.add(book);
            System.out.println("Libro añadido al catálogo: " + book.getTitle());
        } else {
            System.out.println("Solo los administradores pueden añadir libros.");
        }
    }
    
    public void removeBook(Book book, User user) {
        if (user.getRole() instanceof Admin) {
            if (catalog.remove(book)) {
                System.out.println("Libro eliminado: " + book.getTitle());
            } else {
                System.out.println("El libro no está en el catálogo.");
            }
        } else {
            System.out.println("Solo los administradores pueden eliminar libros.");
        }
    }
    
    public Book findBook(String title) {
        for (Book book : catalog) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                return book;
            }
        }
        return null;
    }
    
    public void showAvailableBooks() {
        System.out.println("Libros disponibles en la biblioteca:");
        boolean available = false;
        
        for (Book book : catalog) {
            if (!book.isBorrowed()) {
                System.out.println("- " + book.description());
                available = true;
            }
        }
        
        if (!available) {
            System.out.println("No hay libros disponibles en este momento.");
        }
    }
    
    public void showAllBooks() {
        System.out.println("Todos los libros en el catálogo:");
        for (Book book : catalog) {
            System.out.println("- " + book.description());
        }
    }
}
