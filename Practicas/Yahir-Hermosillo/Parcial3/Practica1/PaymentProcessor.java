public class PaymentProcessor {
    public static void processPayment(PaymentMethod method, double amount) {
        method.processPayment(amount);
    }
    
    public static void main(String[] args) {
        // Crear instancias de los diferentes métodos de pago
        PaymentMethod tarjeta = new CreditCardPayment("1234567812345678", "12/25", "123");
        PaymentMethod paypal = new PayPalPayment("usuario@example.com", "secreto");
        PaymentMethod transferencia = new BankTransferPayment("987654321", "123456789");
        
        // Procesar pagos con diferentes montos
        processPayment(tarjeta, 150.0);
        processPayment(paypal, 75.5);
        processPayment(transferencia, 200.0);
        
        // Probar con otros montos
        processPayment(tarjeta, 99.99);
        processPayment(paypal, 50.0);   
        processPayment(transferencia, 1000.0);
    }
}