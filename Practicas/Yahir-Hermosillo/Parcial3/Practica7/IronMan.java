public class IronMan extends MarvelCharacter {
    public IronMan(String name, String alias, String universe, int age) {
        super(name, alias, universe, age);
    }

    @Override
    public void showPower() {
        System.out.println("Tengo mi armadura de nanotecnología");
    }
}