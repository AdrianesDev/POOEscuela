public class SpiderMan extends MarvelCharacter {
    public SpiderMan(String name, String alias, String universe, int age) {
        super(name, alias, universe, age);
    }

    @Override
    public void showPower() {
        System.out.println("¡Puedo lanzar telarañas y trepar paredes!");
    }
}
