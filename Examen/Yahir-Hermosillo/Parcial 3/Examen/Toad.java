public class Toad {
    private int cantidadDePlatanos = 3;
    
    public void lanzarPlatano() {
        if (cantidadDePlatanos > 0) {
            cantidadDePlatanos -= 1;
            System.out.println("¡Toad lanza un platano! Quedan " + cantidadDePlatanos);
        } else {
            System.out.println("No quedan platanos");
        }
    }
    
    public void recargarPlatanos() {
        cantidadDePlatanos = 3;
        System.out.println("¡Platanos recargados! Toad tiene " + cantidadDePlatanos + " plátanos");
    }
}