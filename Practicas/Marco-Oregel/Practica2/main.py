from Client import Client
from Product import Product
from Order import Order

client = Client("Marco Oregel")

product1 = Product("Burrito", 20 )
product2 = Product("Sushi", 80)
product3 = Product("Pizza", 100.25)

client.placeAnOrder([product1, product2])
client.placeAnOrder([product2, product3])

for i in range(len(client.orders)):
        order = client.orders[i]
        print(f"Cliente: {client.name}")
        print(f"Pedido {i + 1}:")
       
        for product in order.products:
            print(f"  - {product.name} = ${product.price}")
        
        print(f"Total del Pedido {i + 1}: ${order.calculateTotal()}")
        print("-" * 40)