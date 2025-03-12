from abc import ABC, abstractmethod

class PaymentMethod(ABC):

   @abstractmethod
   def process_payment(self, amount: float):
       pass

class CreditCardPayment(PaymentMethod):
   def __init__(self, card_name, card_number, cvv, expiration_date):
       self.card_name = card_name
       self.__card_number = card_number
       self.__cvv = cvv
       self.__expiration_date = expiration_date

   def process_payment(self, amount: float):
       print(f"Procesando su pago con tarjeta por el monto de ${amount}")
       print(f"Su pago ha sido procesado por el monto de ${amount}")
       return "Pago con tarjeta exitoso"

   @property
   def card_number(self):
       masked = "*" * (len(self.__card_number) - 4) + self.__card_number[-4:]
       return masked
   
   @card_number.setter
   def card_number(self, card_number):
       self.__card_number = card_number

   @property
   def cvv(self):
       return self.__cvv
   
   @cvv.setter
   def cvv(self, cvv):
       self.__cvv = cvv

   @property
   def expiration_date(self):
       return self.__expiration_date
   
   @expiration_date.setter
   def expiration_date(self, expiration_date):
       self.__expiration_date = expiration_date

   
class PayPalPayment(PaymentMethod):
   def __init__(self, email, password):
       self.__email = email
       self.__password = password

   def process_payment(self, amount: float):
       print(f"Procesando su pago con PayPal por el monto de ${amount}")
       print(f"Su pago con PayPal ha sido realizado por el monto de ${amount}")
       return "Pago con PayPal exitoso"

   @property
   def email(self):
       return self.__email
   
   @email.setter
   def email(self, email):
       self.__email = email
   
   @property
   def password(self):
       return "********"
   
   @password.setter
   def password(self, password):
       self.__password = password

class BankTransferPayment(PaymentMethod):
   def __init__(self, account_number, bank_name):
       self.__account_number = account_number
       self.bank_name = bank_name

   def process_payment(self, amount: float):
       print(f"Procesando su pago por transferencia bancaria por ${amount}")
       print(f"Pago con transferencia bancaria realizado por ${amount}")
       return "Pago con transferencia bancaria exitoso"

   @property
   def account_number(self):
       masked = "*" * (len(self.__account_number) - 3) + self.__account_number[-3:]
       return masked
   
   @account_number.setter
   def account_number(self, account_number):
       self.__account_number = account_number

def process_payment(payment_method, amount):
   print(f"\nProcesando pago de ${amount:.2f}")
   result = payment_method.process_payment(amount)
   print(f"Resultado: {result}")
   print("-" * 50)
   return result

credit_card = CreditCardPayment("Juan Avilez", "1234-5678-9012-3456", "786", "12/26")
paypal = PayPalPayment("avilezcapi@paypal.com", "contraseña123")
bank_transfer = BankTransferPayment("987654321", "BBVA")

process_payment(credit_card, 2000.0)
process_payment(paypal, 500.0)
process_payment(bank_transfer, 200.0)

print(credit_card.card_number)
print("-" * 50)
credit_card.card_number = "5678-1234-5678-1234"
print(credit_card.card_number)
print("-" * 50)