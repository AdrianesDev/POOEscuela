class BankTransferPayment extends PaymentMethod {
    private String accountNumber;
    private String routingNumber;
    
    public BankTransferPayment(String accountNumber, String routingNumber) {
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
    }
    
    @Override
    public void processPayment(double amount) {
        System.out.printf("Procesando transferencia bancaria de $%.2f - Cuenta: ****%s%n",
                          amount, accountNumber.substring(accountNumber.length() - 4));
    }
}