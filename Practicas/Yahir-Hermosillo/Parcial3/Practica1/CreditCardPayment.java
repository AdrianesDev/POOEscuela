class CreditCardPayment extends PaymentMethod {
    private String cardNumber;
    private String expirationDate;
    private String cvv;
    
    public CreditCardPayment(String cardNumber, String expirationDate, String cvv) {
        this.cardNumber = cardNumber;
        this.expirationDate = expirationDate;
        this.cvv = cvv;
    }
    
    @Override
    public void processPayment(double amount) {
        System.out.printf("Procesando pago con tarjeta de $%.2f - Número: ****%s%n", 
                         amount, cardNumber.substring(cardNumber.length() - 4));
    }
}