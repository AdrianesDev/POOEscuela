public class Mascota {
    private String nombre;
    private String tipo;
    private int edad;
    private boolean estaAdoptado;
    
    // Constructor
    public Mascota(String nombre, String tipo, int edad) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.edad = edad;
        this.estaAdoptado = false; // Por defecto no esta adoptado
    }
    
    // Metodo para obtener la descripción
    public String descripcion() {
        String estado = estaAdoptado ? "Adoptado" : "No adoptado";
        return nombre + " es un " + tipo + " de " + edad + " años. Estado: " + estado + ".";
    }
    
    // Metodo para adoptar la mascota
    public void adoptar() {
        estaAdoptado = true;
    }
    
    // Metodos getters
    public String getNombre() {
        return nombre;
    }
    
    public String getTipo() {
        return tipo;
    }
    
    public int getEdad() {
        return edad;
    }
    
    public boolean getEstaAdoptado() {
        return estaAdoptado;
    }
}