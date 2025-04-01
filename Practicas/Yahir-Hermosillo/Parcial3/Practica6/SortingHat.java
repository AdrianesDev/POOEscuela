import java.util.Random;

public class SortingHat {
    private static final String[] HOUSES = {
        "Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"
    };

    public void assignHouse(MagicPerson person) {
        Random random = new Random();
        String house = HOUSES[random.nextInt(HOUSES.length)];
        person.setHouse(house);
        System.out.println("¡" + person.getName() + ", serás de... " + house.toUpperCase() + "!");
    }
}