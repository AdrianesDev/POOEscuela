public class Client {
    String name;
    Order[] orders;
    int orderCount;

    public Client(String name) {
        this.name = name;
        this.orders = new Order[10]; // Asumimos un máximo de 10 pedidos por cliente
        this.orderCount = 0;
    }

    public void placeAnOrder(Product[] products) {
        if (orderCount < orders.length) {
            orders[orderCount] = new Order(products);
            orderCount++;
        } else {
            System.out.println("No se pueden agregar más pedidos.");
        }
    }
}
