import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Student extends MagicPerson {
    private int yearsAtHogwarts;
    private List<Spell> favoriteSpells;

    public Student(String name, int age, int yearsAtHogwarts) {
        super(name, age);
        this.yearsAtHogwarts = yearsAtHogwarts;
        this.favoriteSpells = new ArrayList<>();
    }

    public int getYearsAtHogwarts() {
        return yearsAtHogwarts;
    }

    public void addFavoriteSpell(Spell spell) {
        favoriteSpells.add(spell);
    }

    @Override
    public void castSpell() {
        if (favoriteSpells.isEmpty()) {
            System.out.println(getName() + " no conoce ningún hechizo todavía.");
        } else {
            Random random = new Random();
            Spell randomSpell = favoriteSpells.get(random.nextInt(favoriteSpells.size()));
            System.out.print(getName() + " lanza el hechizo: ");
            randomSpell.cast();
        }
    }
}