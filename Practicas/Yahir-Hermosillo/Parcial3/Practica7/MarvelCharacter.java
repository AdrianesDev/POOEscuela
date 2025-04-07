public class MarvelCharacter {
    private String name;
    private String alias;
    private String universe;
    private int age;

    public MarvelCharacter(String name, String alias, String universe, int age) {
        this.name = name;
        this.alias = alias;
        this.universe = universe;
        if (age > 0) {
            this.age = age;
        } else {
            this.age = 0;
        }
    }

    public void showPower() {
        System.out.println("Este personaje tiene poderes especiales.");
    }

    public int getAge() {
        return age;
    }

    public void updateAge(int newAge) {
        if (newAge > 0) {
            this.age = newAge;
        }
    }
}
