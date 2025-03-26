public class Order {
    Product[] products;

    public Order(Product[] products) {
        this.products = products;
    }

    public double calculateTotal() {
        double total = 0;
        for (Product product : products) {
            total += product.price;
        }
        return total;
    }
}
