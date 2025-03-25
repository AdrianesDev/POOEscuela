public class Main {
    public static void main(String[] args) {
        // Crear la biblioteca
        Library library = new Library();
        
        // Crear usuarios con diferentes roles
        User admin = new User("Ana", new Admin());
        User user1 = new User("Carlos", new RegularUser());
        User guest = new User("Invitado", new Guest());
        
        // Admin añade libros
        Book book1 = new Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez");
        Book book2 = new Book("1984", "George Orwell");
        Book book3 = new Book("The Little Prince", "Antoine de Saint-Exupery");
        
        library.addBook(book1, admin);
        library.addBook(book2, admin);
        library.addBook(book3, admin);
        
        System.out.println("\n--- Estado inicial ---");
        library.showAllBooks();
        System.out.println();
        
        // Usuario intenta prestar libros
        System.out.println("\n--- Préstamos ---");
        user1.borrowBook(book1);
        user1.borrowBook(book2);
        user1.borrowBook(book3);
        
        // Intentar prestar un cuarto libro
        Book book4 = new Book("Don Quijote", "Miguel de Cervantes");
        library.addBook(book4, admin);
        user1.borrowBook(book4); // No debería permitir
        
        // Invitado intenta prestar un libro
        guest.borrowBook(book1);
        
        System.out.println("\n--- Estado después de préstamos ---");
        library.showAvailableBooks();
        user1.showBorrowedBooks();
        
        // Devolver un libro
        System.out.println("\n--- Devoluciones ---");
        user1.returnBook(book2);
        
        System.out.println("\n--- Estado final ---");
        library.showAvailableBooks();
        user1.showBorrowedBooks();
    }
}