public class Spell {
    private String name;
    private String description;

    public Spell(String name, String description){
        this.name = name;
        this.description = description;
    }

    public void cast(){
        System.out.println("¡" + name + "! " + description);
    }

    public String getName(){
        return name;
    }
    
}
