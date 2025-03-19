from typing import Protocol

class PaymentMethod(Protocol):

    def __init__(self,amount = 0.0):
        self._amount = amount
        

    def processPayment(self,_amount):
        print(f"Se ha procesado su pago de: $ {self._amount}")

