#include <iostream>
#include <memory>

using namespace std;

class PaymentMethod {
public:
    virtual void processPayment(double amount) const = 0; 
    virtual ~PaymentMethod() {}
};

class CreditCardPayment : public PaymentMethod {
private:
    string cardNumber;
public:
    CreditCardPayment(const string& card) : cardNumber(card) {}
    void processPayment(double amount) const override {
        cout << "Processing credit card payment of $" << amount << " using card: **** **** **** " << cardNumber.substr(cardNumber.length() - 4) << endl;
    }
};

class PayPalPayment : public PaymentMethod {
private:
    string email;
public:
    PayPalPayment(const string& email) : email(email) {}
    void processPayment(double amount) const override {
        cout << "Processing PayPal payment of $" << amount << " using email: " << email << endl;
    }
};

class BankTransferPayment : public PaymentMethod {
private:
    string accountNumber;
public:
    BankTransferPayment(const string& account) : accountNumber(account) {}
    void processPayment(double amount) const override {
        cout << "Processing bank transfer payment of $" << amount << " from account: ****" << accountNumber.substr(accountNumber.length() - 4) << endl;
    }
};

void makePayment(const PaymentMethod& paymentMethod, double amount) {
    paymentMethod.processPayment(amount);
}

int main() {
    CreditCardPayment creditCard("1234567812345678");
    PayPalPayment paypal("user@example.com");
    BankTransferPayment bankTransfer("9876543210");

    makePayment(creditCard, 100.50);
    makePayment(paypal, 75.25);
    makePayment(bankTransfer, 200.00);
    
    return 0;
}
