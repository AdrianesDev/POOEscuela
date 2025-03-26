class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"
    
class Order:
    def __init__(self, products):
        self.products = products 
    
    def add_product (self, product):
        self.products.append(product)
    def get_products(self):
        return self.products
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
class Client:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def get_name(self):
        return self.name
    def get_orders(self):
        return self.orders
    def place_an_order(self,products):
        new_order = Order(products)
        self.orders.append(new_order)
        return  new_order
    
if __name__ == "__main__":
    tacos = Product("Orden de tacos de Asada", 100)
    papa = Product("Papa al horno", 80)
    bebida = Product("Agua de coco con nuez", 40)

    client = Client("Juan Avilez")

    order = client.place_an_order([tacos, papa, bebida])

    print(f"Client Name: {client.get_name()}\n")
    print("Order Details: ")
    for product in order.get_products():
        print(product)

    print(f"\n Total: ${order.calculate_total():.2f}")
    print("--"*20)

if __name__ == "__main__":
    tacos = Product("Orden de tacos de adobada", 120)
    burrito = Product("Mega burrito de asada", 150)
    tacos = Product("5 Tacos de birria", 130)
    bebidas = Product("2 Aguas de jamaica", 160)

    client = Client ("Manuel Lopez")

    order = client.place_an_order([tacos, burrito, tacos, bebidas])

    print(f"Client Name: {client.get_name()}\n")
    print("Order Details: ")
    for product in order.get_products():
        print(product)

    print(f"\n Total: ${order.calculate_total():.2f}")
