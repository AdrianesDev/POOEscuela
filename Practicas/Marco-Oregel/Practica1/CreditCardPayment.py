from PaymentMethod import PaymentMethod

class CreditCardPayment(PaymentMethod):

    def __init__(self,number,name,date,cvv):
        self._number = number
        self._name = name
        self._date = date
        self._cvv = cvv

    def processPayment(self,amount):
        print(f"Se ha procesado su pago de: $ {amount} pesos con tarjeta de credito de: {self._name}")
