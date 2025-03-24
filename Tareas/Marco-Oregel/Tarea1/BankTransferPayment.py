from PaymentMethod import PaymentMethod

class BankTransferPayment(PaymentMethod):

    def __init__(self,user,password,account_number,description):
        self._user = user
        self._password = password
        self._account_number = account_number
        self._description = description

    def processPayment(self,amount):
        print(f"Se ha procesado su pago de: $ {amount} pesos con transferencia bancaria desde la cuenta de: {self._user}, a la cuenta: {self._account_number}")