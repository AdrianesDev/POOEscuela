class Product():
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order():
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)


    def calculateTotal(self):
        total = sum(product.price for product in self.products)
        return total

class Client():
    def __init__(self,name):
        self.name = name
        self.orders = []

    def placeAnOrder(self,order):
        self.orders.append(order)

    def calculateOrders(self):
        total_orders = sum(order.calculateTotal() for order in self.orders)
        return total_orders
    
product1 = Product('Hamburguer', 15.90)
product2 = Product('Pizza', 2.45)
product3 = Product('Hot Dog', 3.50)

order1 = Order()
order1.add_product(product1)
order1.add_product(product2)

order2 = Order()
order2.add_product(product2)

client = Client('Carlos')
client.placeAnOrder(order1)
client.placeAnOrder(order2)

print(f"El total de {client.name} es: ${client.calculateOrders():.2f}")
print(f"Total del pedido: ${order1.calculateTotal():.2f}")