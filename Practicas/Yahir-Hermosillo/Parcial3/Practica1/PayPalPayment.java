class PayPalPayment extends PaymentMethod {
    private String email;
    private String password;
    
    public PayPalPayment(String email, String password) {
        this.email = email;
        this.password = password;
    }
    
    @Override
    public void processPayment(double amount) {
        System.out.printf("Procesando pago con PayPal de $%.2f - Email: %s%n", amount, email);
    }
}