from abc import ABC, abstractclassmethod
class PaymentMethod(ABC):
    @abstractclassmethod
    def processPayment(self, cantidad):
        pass
 
class CreditCardPayment(PaymentMethod):
        def __init__(self, name, number, cvv, expiration):
          self.name = name
          self.number = number
          self.cvv = cvv
          self.expiration = expiration
        def processPayment(self, cantidad):
            print(f"procesando pago de {cantidad} con tarjeta de creadito de {self.name}.")
  
    


class PayPalPayment(PaymentMethod):
    def __init__(self, email, password ):
        self.email = email
        self.password = password
    def processPayment(self, cantidad):
        print(f"procesando pago de {cantidad} con paypal de la cuenta{self.email}.")





class BankTransferPayment(PaymentMethod):
    def __init__(self, cuenta):
        self.cuenta = cuenta
    def processPayment(self , cantidad):
        print(f"procesando pago de {cantidad} desde la cuenta {self.cuenta}")
def proceso(proceso, cantidad):

    proceso.processPayment(cantidad)

credito = CreditCardPayment("ignacio", "1234567890123456", "123", "12/25")
paypal = PayPalPayment("ignacio@gmail.com", "1234")
transferencia = BankTransferPayment("9876543210")  

proceso(credito, 100)
proceso(paypal, 50)
proceso(transferencia, 200)