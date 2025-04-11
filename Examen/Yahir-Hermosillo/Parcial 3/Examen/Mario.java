public class Mario extends Corredor{
    @Override
    public void acelerar(){
        velocidad += 10;
        System.out.println("Mario acelera a " + velocidad + " km/h");
    }
    
}
