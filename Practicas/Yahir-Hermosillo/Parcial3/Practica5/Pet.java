public class Pet {
    private String name;
    private String type;
    private int age;
    private boolean isAdopted;
    
    // Constructor
    public Pet(String name, String type, int age) {
        this.name = name;
        this.type = type;
        this.age = age;
        this.isAdopted = false; // Por defecto no esta adoptado
    }
    
    // Metodo para obtener la descripción
    public String descripcion() {
        String status = isAdopted ? "Adoptado" : "No adoptado";
        return name + " es un " + type + " de " + age + " años. Estado: " + status + ".";
    }
    
    // Metodo para adoptar la mascota
    public void adoptar() {
        isAdopted = true;
    }
    
    // Metodos getters
    public String getName() {
        return name;
    }
    
    public String getType() {
        return type;
    }
    
    public int getAge() {
        return age;
    }
    
    public boolean getAdoptionStatus() {
        return isAdopted;
    }
}