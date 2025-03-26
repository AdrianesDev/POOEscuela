from PaymentMethod import PaymentMethod

class PayPalPayment(PaymentMethod):

    def __init__(self,email,password):
        self._email = email
        self._password = password

    def processPayment(self,amount):
        print(f"Se ha procesado su pago de: $ {amount} pesos con PayPal de la cuenta: {self._email}")