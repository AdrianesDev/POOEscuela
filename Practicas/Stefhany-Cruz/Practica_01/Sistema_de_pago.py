from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, ownerName, expitrationDate, cardNumber, securityCode):
        self.ownerName = ownerName 
        self.expirationDate = expitrationDate
        self.__cardNumber = cardNumber 
        self.__securityCode = securityCode

    def get_cardNumber(self):  
        return self.__cardNumber
    
    def get_securityCode(self):
        return self.__securityCode

    def processPayment(self, amount: float):
        print(f"Pago con tarjeta de credito de ${amount} realizado con exito")

class PayPalPayment(PaymentMethod):
    def __init__(self, userName, email):
        self.userName = userName
        self.__email = email  

    def get_email(self):
        return self.__email

    def processPayment(self, amount: float):
        print(f"Pago con Pay Pal de ${amount} realizado con exito")

class BankTransferPayment(PaymentMethod):
    def __init__(self, accountNumber):
        self.__accountNumber = accountNumber 

    def get_accountNumber(self):
        return self.__accountNumber
    
    def processPayment(self, amount: float):
        print(f"Pago mediante transferencia bancaria de ${amount} realizado con exito")

def paymentMethod(pay: PaymentMethod, amount: float):
    pay.processPayment(amount)

pay1 = CreditCardPayment("Stefhany Cruz", "12/28" ,"10031994", "1424")
pay1.processPayment(1946)

pay2 = PayPalPayment("Stefhany Cruz", "cruzdiazstefhany@gmail.com")
pay2.processPayment(258.22)

pay3 = BankTransferPayment("1596327845")
pay3.processPayment(78.50)