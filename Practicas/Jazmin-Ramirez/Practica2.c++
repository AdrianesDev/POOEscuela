#include <iostream>
#include <vector>
#include <string>

using namespace std;


class Product {
public:
    string name;
    double price;

    Product(string name, double price) : name(name), price(price) {}
};


class Order {
public:
    vector<Product> products;

    void addProduct(const Product& product) {
        products.push_back(product);
    }

    double calculateTotal() const {
        double total = 0;
        for (const auto& product : products) {
            total += product.price;
        }
        return total;
    }
};


class Client {
public:
    string name;
    vector<Order> orders;

    Client(string name) : name(name) {}

    void placeAnOrder(const vector<Product>& productList) {
        Order newOrder;
        for (const auto& product : productList) {
            newOrder.addProduct(product);
        }
        orders.push_back(newOrder);
        cout << "Pedido realizado por " << name << ". Total: $" << newOrder.calculateTotal() << endl;
    }
};


int main() {
    
    Product pizza("Pizza", 12.50);
    Product burger("Burger", 8.75);
    Product soda("Soda", 2.50);

    
    Client cliente("Carlos");


    vector<Product> pedido1 = {pizza, soda};
    vector<Product> pedido2 = {burger, soda, pizza};


    cliente.placeAnOrder(pedido1);
    cliente.placeAnOrder(pedido2);
    
    cout << "\nResumen de Pedidos:\n";
    for (size_t i = 0; i < cliente.orders.size(); ++i) {
        cout << "Pedido " << i + 1 << " - Total: $" << cliente.orders[i].calculateTotal() << endl;
    }

    return 0;
}