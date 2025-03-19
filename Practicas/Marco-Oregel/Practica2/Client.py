from Order import Order
from Product import Product
class Client(Order):

    def __init__(self,name):
        self.name = name
        self.orders = []

        
    def placeAnOrder(self,products):
        order = Order()
        for product in products:
            order.addProduct(product)
        self.orders.append(order)
        return order