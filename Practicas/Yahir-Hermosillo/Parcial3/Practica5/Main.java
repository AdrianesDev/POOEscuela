public class Main {
    public static void main(String[] args) {
        // Crear una mascota
        Pet pet1 = new Pet("Firulais", "Perro", 3);
        
        // Mostrar su descripcion
        System.out.println(pet1.descripcion());
        
        // Adoptar la mascota
        pet1.adoptar();
        
        // Mostrar descripcion despues de adoptar
        System.out.println(pet1.descripcion());
    }
}