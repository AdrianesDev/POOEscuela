public class Main {
    public static void main(String[] args) {
        //Crear hechizos
        Spell expelliarmus = new Spell("Expelliamus", "desarma al oponente");
        Spell lumos = new Spell("Lumos", "ilumina la punta de tu varita");
        Spell wingardium = new Spell("Wigardium Leviosa", "hace que los objetos leviten");
        Spell protego = new Spell("Protego", "crea un escudo protector");

        //Crear el sombrero seleccionador
        SortingHat sortingHat = new SortingHat();

        //Crear estudiantes
        Student harry = new Student("Harry Potter", 11, 1);
        Student hermione= new Student("Hermione Granger", 11, 1);
        Student ron = new Student("Ron Wasley", 11, 1);

        //Añadir hechizos a los estudiantes
        harry.addFavoriteSpell(expelliarmus);
        harry.addFavoriteSpell(protego);
        
        hermione.addFavoriteSpell(wingardium);
        hermione.addFavoriteSpell(lumos);
        
        ron.addFavoriteSpell(protego);
        ron.addFavoriteSpell(lumos);

        // Asignar casas
        sortingHat.assignHouse(harry);
        sortingHat.assignHouse(hermione);
        sortingHat.assignHouse(ron);

         // Crear profesores
         Professor dumbledore = new Professor("Albus Dumbledore", 150, "Headmaster");
         Professor mcgonagall = new Professor("Minerva McGonagall", 60, "Transfiguration");
         Professor snape = new Professor("Severus Snape", 38, "Potions");
 
         // Asignar casas a profesores
         dumbledore.setHouse("Gryffindor");
         mcgonagall.setHouse("Gryffindor");
         snape.setHouse("Slytherin");
 
         // Presentaciones
         System.out.println("\n--- Presentaciones ---");
         harry.introduce();
         hermione.introduce();
         ron.introduce();
         dumbledore.introduce();
         mcgonagall.introduce();
         snape.introduce();
 
         // Demostracion de hechizos
         System.out.println("\n--- Demostración de hechizos ---");
         harry.castSpell();
         hermione.castSpell();
         ron.castSpell();
         dumbledore.castSpell();
         mcgonagall.castSpell();
         snape.castSpell();
    }
}
