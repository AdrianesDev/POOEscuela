class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    def __init__(self, products: list):
        self.products = products

    def calculateTotal(self) -> float:
        return sum(product.price for product in self.products)

class Client:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def placeAnOrder(self, products: list):
        order = Order(products)
        self.orders.append(order)
        return order

product1 = Product("Pizza", 339.82)
product2 = Product("Tacos", 35.56)
product3 = Product("Sushi", 502.27)
product4 = Product("Hot dogs", 60.22)
product5 = Product("Hamburguesa", 294.77)
product6 = Product("Papas fritas", 99.99)

client = Client("Stefhany Cruz")

order1 = client.placeAnOrder([product2, product4])
order2 = client.placeAnOrder([product5, product6])
order3 = client.placeAnOrder([product1, product3])

print(f"Cliente: {client.name}")
print(f"Total del primer pedido: ${order1.calculateTotal()}")
print(f"Total del segundo pedido: ${order2.calculateTotal()}")
print(f"Total del tercer pedido: ${order3.calculateTotal()}")