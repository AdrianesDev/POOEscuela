public class Professor extends MagicPerson {
    private String subject;

    public Professor(String name, int age, String subject) {
        super(name, age);
        this.subject = subject;
    }

    @Override
    public void castSpell() {
        System.out.println(getName() + ", profesor de " + subject + ", lanza un hechizo especial para enseñar.");
    }
}
