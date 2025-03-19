from PaymentMethod import PaymentMethod
from PayPalPayment import PayPalPayment
from CreditCardPayment import CreditCardPayment
from BankTransferPayment import BankTransferPayment
    

transferencia = BankTransferPayment("Marco45","4455","0123456789","Colegiatura")
paypal = PayPalPayment("Marcoore444@gmail.com","1234")
credito = CreditCardPayment("2125484764852415","Marco Oregel", "05/27","225")

transferencia.processPayment(10500)
paypal.processPayment(5050)
credito.processPayment(2042)

