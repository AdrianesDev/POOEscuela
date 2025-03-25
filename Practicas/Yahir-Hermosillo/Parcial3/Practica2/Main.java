public class Main {
    public static void main(String[] args){
        //Crear productos
        Product pizza = new Product("Pizza", 10.99);
        Product burger = new Product("Burger", 5.99);
        Product soda = new Product("Soda", 1.99);

        //Crear un cliente
        Client client = new Client("Juan");

        //Crear dos pedidos
        Product[] order1Products = {pizza, soda};
        Product[] order2Products = {burger, soda};

        client.placeAnOrder(order1Products);
        client.placeAnOrder(order2Products);

        //Imprimir el total de cada pedido
        for (int i = 0; i < client.orderCount; i++){
            System.out.println("Total del pedido "+(i + 1) + ": $" + client.orders[i].calculateTotal());
        }
    }
}
