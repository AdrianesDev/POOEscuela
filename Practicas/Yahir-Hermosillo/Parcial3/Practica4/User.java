import java.util.ArrayList;

public class User {
    private String name;
    private ArrayList<Book> borrowedBooks;
    private Role role;
    
    public User(String name, Role role) {
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
        this.role = role;
    }
    
    public String getName() {
        return name;
    }
    
    public Role getRole() {
        return role;
    }
    
    public void borrowBook(Book book) {
        if (role instanceof Guest) {
            System.out.println("Los invitados no pueden tomar prestados libros.");
            return;
        }
        
        if (borrowedBooks.size() >= 3) {
            System.out.println("No puedes tener más de 3 libros prestados.");
            return;
        }
        
        if (book.isBorrowed()) {
            System.out.println("El libro ya está prestado.");
            return;
        }
        
        book.setBorrowed(true);
        borrowedBooks.add(book);
        System.out.println(name + " ha tomado prestado: " + book.getTitle());
    }
    
    public void returnBook(Book book) {
        if (borrowedBooks.remove(book)) {
            book.setBorrowed(false);
            System.out.println(name + " ha devuelto: " + book.getTitle());
        } else {
            System.out.println("Este usuario no tiene prestado ese libro.");
        }
    }
    
    public void showBorrowedBooks() {
        System.out.println("Libros prestados a " + name + ":");
        if (borrowedBooks.isEmpty()) {
            System.out.println("Ninguno");
        } else {
            for (Book book : borrowedBooks) {
                System.out.println("- " + book.description());
            }
        }
    }
}
