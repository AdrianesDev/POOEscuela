class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"
    
class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_total(self) -> float:
        return sum(product.price for product in self.products)

    def __str__(self):
        products_str = "\n".join([f"  - {product}" for product in self.products])
        return f"Order:\n{products_str}\nTotal: ${self.calculate_total():.2f}"


class Client: 
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def place_an_order(self, products: list[Product]):
        order = Order()
        for product in products:
            order.add_product(product)
        self.orders.append(order)
        print(f"Order placed by {self.name}")

    def show_orders(self):
        print(f"\nOrders for {self.name}:")
        for i, order in enumerate(self.orders, start=1):
            print(f"Order {i}:")
            print(order)

if __name__ == "__main__":

    product = Product("Hamburguesa clasica", 80)
    product2 = Product("Hamburguesa c/ queso", 120)
    product3 = Product("Hamburguesa doble carne", 160)
    product4 = Product("Hamburguesa doble carne doble queso", 200)
    product5 = Product("Hamburguesa de pollo", 90)
    Product6 = Product("Papas fritas", 50) 
    Product7 = Product("Soda", 50)

    client = Client("Elit-Aniceto")

    client.place_an_order([product, product2])  
    client.place_an_order([product3, product4])

    client.show_orders()