from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.__card_number = card_number
        self.__expiration_date = expiration_date
        self.__cvv = cvv

    def processPayment(self, amount: float):
        print(f"Procesando pago de ${amount} tarjeta de credito con terminacion {self.__card_number[-4:]}")

class PaypalPayment(PaymentMethod):
    def __init__(self, phone_number: str, email: str):
        self.__phone_number = phone_number
        self.__email = email

    def processPayment(self, amount: float):
        print(f"Procesando pago de ${amount} app Paypal asociado al numero {self.__phone_number} con email {self.__email}")

class BankTransferPayment(PaymentMethod):
    def __init__(self, account_number: str, bank_name: str):
        self.__account_number = account_number
        self.__bank_name = bank_name

    def processPayment(self, amount: float):
        print(f"Procesando pago de ${amount} transferencia a la cuenta {self.__account_number} en {self.__bank_name}")

def process_payment(payment_method: PaymentMethod, amount: float):
        payment_method.processPayment(amount)

        
credit_card_payment = CreditCardPayment("1223099834874576", "12/27", "247")
paypal_payment = PaypalPayment("6647194013", "elitaniceto@gmail.com")
bank_transfer_payment = BankTransferPayment("102938475", "BBVA")

process_payment(credit_card_payment, 1000.0)
process_payment(paypal_payment, 3000.0)
process_payment(bank_transfer_payment, 5000.0)
        
        
        