from Product import Product
class Order(Product):
   
   def __init__(self):
        self.products = []

   def addProduct(self, product):
        self.products.append(product)

   def calculateTotal(self):
     return sum(product.price for product in self.products)