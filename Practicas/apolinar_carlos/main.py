from typing import Protocol

class PaymentMetod(Protocol):
    def processPayment(self, amount: float):
        pass

class CreditCardPayment(PaymentMetod):
    def __init__(self, card_number, holder_card, expiration_date, cvv):
        self.__card_number = card_number
        self.__holder_card = holder_card
        self.__expiration_date = expiration_date
        self.__cvv = cvv

    def processPayment(self, amount: float):
        print(f"El pago se procesara de {amount} de su tarjeta de credito.")

        print(f"Pago realizado con tarjeta de credito.")

        pass



class PaypalPayment(PaymentMetod):
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        
    def processPayment(self, amount: float):
        print(f"El pago se procesara de {amount} de su cuenta de PayPal.")

        print(f"Pago realizado con su cuenta de PayPal.")

        pass

class BankTransferPayment(PaymentMetod):
    def __init__(self, BankAccount):
        self.__BankAccount = BankAccount

    def processPayment(self, amount: float):
        print(f"El pago se procesara la transferencia de {amount} de su cuenta bancaria.")

        print(f"Pago realizado con su cuenta bancaria.")

def process_payment(payment_method: PaymentMetod, amount: float):
    payment_method.processPayment(amount)




credit_card_payment = CreditCardPayment('5544 2222 3059 4032', 'Carlos Apolinar','02/25','212')
paypal_payment = PaypalPayment('emailinsano@gmail.com','contrasegura')
bank_payment = BankTransferPayment('012180007453000182')

process_payment(credit_card_payment, 250.60)
process_payment(paypal_payment, 500.50)
process_payment(bank_payment, 700.00)
