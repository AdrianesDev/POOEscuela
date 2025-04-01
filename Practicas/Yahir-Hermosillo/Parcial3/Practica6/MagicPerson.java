public class MagicPerson {
    private String name;
    private int age;
    private String house;

    public MagicPerson(String name, int age){
        this.name = name;
        this.age = age;
    }

    public void introduce() {
        System.out.println("Hola, soy " + name + ", tengo " + age + " años" + 
                          (house != null ? " y soy de " + house : "") + ".");
    }
           
        
    public void castSpell() {
        System.out.println(name + " lanza un hechizo genérico.");
    }

    public String getName() {
        return name;
    }

    public void setHouse(String house) {
        this.house = house;
    }
}
