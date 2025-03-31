// Book.java
public class Book {
    private String title;
    private String author;
    private boolean isBorrowed;
    
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isBorrowed = false;
    }
    
    public String getTitle() {
        return title;
    }
    
    public String getAuthor() {
        return author;
    }
    
    public boolean isBorrowed() {
        return isBorrowed;
    }
    
    public void setBorrowed(boolean borrowed) {
        isBorrowed = borrowed;
    }
    
    public String description() {
        return title + " por " + author + " - " + (isBorrowed ? "Prestado" : "Disponible");
    }
}