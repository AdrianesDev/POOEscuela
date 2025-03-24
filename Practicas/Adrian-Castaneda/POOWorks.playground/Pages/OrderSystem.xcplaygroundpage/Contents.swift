class Product {
    let name: String
    let price: Double

    init(name: String, price: Double) {
        self.name = name
        self.price = price
    }
}

class Order {
    let products: [Product]

    init(products: [Product]) {
        self.products = products
    }

    func calculateTotal() -> Double {
        return products.reduce(0) { $0 + $1.price }
    }
}

class Client {
    let name: String
    var orders: [Order] = []

    init(name: String) {
        self.name = name
    }

    func placeAnOrder(products: [Product]) {
        let newOrder = Order(products: products)
        orders.append(newOrder)
        print("Order placed by \(name). Total: \(newOrder.calculateTotal())")
    }
}

let burgers = Product(name: "Burger", price: 8.99)
let pizza = Product(name: "Pizza", price: 12.50)
let sodas = Product(name: "Soda", price: 2.50)


let client1 = Client(name: "Adrián")

client1.placeAnOrder(products: [burgers, sodas])
client1.placeAnOrder(products: [pizza, sodas])

for (index, order) in client1.orders.enumerated() {
    print("order \(index + 1): \(order.calculateTotal())")
}
