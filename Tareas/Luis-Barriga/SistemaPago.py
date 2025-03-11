from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self):
        self.__transaction_id = "Luis123"
        self.__amount = 0 
    
    @abstractmethod
    def processPayment(self, amount: float):
        pass 
    
    def getTransactionId(self):
        return self.__transaction_id

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str, card_holder: str):
        super().__init__()
        self.__card_number = card_number
        self.__card_holder = card_holder

    def processPayment(self, amount: float):
        self._PaymentMethod__amount = amount  
        print(f"Procesando pago de ${self._PaymentMethod__amount} con tarjeta de credito")
        print(f"Pago exitoso con tarjeta: {self.__card_number[-4:]}")
        print(f"Transacción ID: {self.getTransactionId()}")

class PayPalPayment(PaymentMethod):
    def __init__(self, email: str):
        super().__init__()
        self.__email = email

    def processPayment(self, amount: float):
        self._PaymentMethod__amount = amount 
        print(f"Procesando pago de ${self._PaymentMethod__amount} con PayPal")
        print(f"Pago exitoso con PayPal. Usuario: {self.__email}")
        print(f"Transacción ID: {self.getTransactionId()}")

class BankTransferPayment(PaymentMethod):
    def __init__(self, account_number: str, bank_name: str):
        super().__init__()
        self.__account_number = account_number
        self.__bank_name = bank_name
    
    def processPayment(self, amount: float):
        self._PaymentMethod__amount = amount  
        print(f"Procesando pago de ${self._PaymentMethod__amount} por transferencia bancaria")
        print(f"Pago exitoso desde cuenta: {self.__account_number[-4:]}")
        print(f"Banco: {self.__bank_name}")
        print(f"Transacción ID: {self.getTransactionId()}")

def process_payment(payment_method: PaymentMethod, amount: float):
    payment_method.processPayment(amount)

credit_card_payment = CreditCardPayment("1234567891728382", "Luis BM")
paypal_payment = PayPalPayment("luis60bf@gmail.com")
bank_transfer_payment = BankTransferPayment("032180000118000019", "BBVA")

process_payment(credit_card_payment, 1000.00)
process_payment(paypal_payment, 1.00)
process_payment(bank_transfer_payment, 10000.00)