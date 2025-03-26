public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        
        // Add books
        library.addBook(new Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez"));
        library.addBook(new Book("The Little Prince", "Antoine de Saint-Exupery"));
        library.addBook(new Book("Don Quixote", "Miguel de Cervantes"));
        
        // Create user Yahir
        User user = new User("Yahir");
        
        // Borrow books
        Book book1 = library.findBook("The Little Prince");
        if(book1 != null) user.borrowBook(book1);
        
        Book book2 = library.findBook("Don Quixote");
        if(book2 != null) user.borrowBook(book2);
        
        Book book3 = library.findBook("One Hundred Years of Solitude");
        if(book3 != null) user.borrowBook(book3);
        
        // Show initial status
        System.out.println("Books borrowed by " + user.getName() + ":");
        for(Book book : user.getBorrowedBooks()) {
            System.out.println("- '" + book.getTitle() + "' by " + book.getAuthor() + " - Borrowed");
        }
        System.out.println();
        
        System.out.println("Available books:");
        library.showAvailableBooks();
        System.out.println();
        
        // Return and borrow
        user.returnBook(book2);
        Book book4 = library.findBook("Fahrenheit 451");
        if(book4 != null) user.borrowBook(book4);
        
        // Show final status
        System.out.println("Books borrowed by " + user.getName() + ":");
        for(Book book : user.getBorrowedBooks()) {
            System.out.println("- '" + book.getTitle() + "' by " + book.getAuthor() + " - Borrowed");
        }
        System.out.println();
        
        System.out.println("Available books:");
        library.showAvailableBooks();
    }
}
