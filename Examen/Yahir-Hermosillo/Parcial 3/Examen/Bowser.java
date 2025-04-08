public class Bowser extends Corredor {
    @Override
    public void acelerar() {
        velocidad += 7;
        System.out.println("Bowser avanza pesadamente a " + velocidad + " km/h");
    }
}
