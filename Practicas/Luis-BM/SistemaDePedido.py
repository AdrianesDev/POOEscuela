class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Order:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def calculateTotal(self):
        total = sum(product.price for product in self.products)
        return total

class Client:
    def __init__(self, name):
        self.name = name
        self.orders = []  

    def placeAnOrder(self, products):
        order = Order()  
        for product in products:
            order.addProduct(product) 
        self.orders.append(order) 
        return order  


HotDog = Product("Hot Dog", 50.00)
Pizza = Product("Pizza", 150.00)
Hamburguesa = Product("Hamburguesa", 250.00)
Taco = Product("Taco", 35.00)


Cliente = Client("Luis BM")


pedido1 = Cliente.placeAnOrder([HotDog, Pizza, Hamburguesa, Taco])
pedido2 = Cliente.placeAnOrder([Taco, Pizza, HotDog])


print(f"Total del pedido 1: ${pedido1.calculateTotal():.2f}")
print(f"Total del pedido 2: ${pedido2.calculateTotal():.2f}")