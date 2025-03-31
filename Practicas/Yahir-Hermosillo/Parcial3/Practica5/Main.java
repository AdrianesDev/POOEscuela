public class Main {
    public static void main(String[] args) {
        // Crear una mascota
        Mascota mascota1 = new Mascota("Firulais", "Perro", 3);
        
        // Mostrar su descripcion
        System.out.println(mascota1.descripcion());
        
        // Adoptar la mascota
        mascota1.adoptar();
        
        // Mostrar descripcion despues de adoptar
        System.out.println(mascota1.descripcion());
    }
}