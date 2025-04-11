public class Main {
    public static void main(String[] args) {
        IronMan tony = new IronMan("Tony Stark", "Iron Man", "MCU", 45);
        SpiderMan peter = new SpiderMan("Peter Parker", "Spider-Man", "MCU", 17);

        showHeroPower(tony);
        showHeroPower(peter);

        System.out.println("La edad de Iron Man es: " + tony.getAge());
        tony.updateAge(-5);
        System.out.println("Ahora Iron Man tiene: " + tony.getAge());
    }

    public static void showHeroPower(MarvelCharacter character){
        character.showPower();
    }
}
