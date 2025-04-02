import random 

class Spell:
    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def cast(self):
        print(f"{self.name}: {self.description}")

class MagicPerson:
    def __init__(self, name, age, house=None):
        self.name = name 
        self.age = age 
        self.house = house

    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}, House: {self.house if self.house else 'Not sorted yet'}")

    def castSpell(self):
        pass 
        
class Student(MagicPerson):
    def __init__(self, name, age, house, yearsAtHogwarts, favoriteSpells):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = yearsAtHogwarts
        self.favoriteSpells = favoriteSpells  

    def castSpell(self):
       if self.favoriteSpells:
            spell = random.choice(self.favoriteSpells)
            spell.cast()
       else:
            print(f"{self.name} has no favorite spells to cast!")

class Professor(MagicPerson):
    def __init__(self, name, age, subject, house="Hogwarts Staff"):
        super().__init__(name, age, house)
        self.subject = subject

    def castSpell(self):
        print(f"Professor {self.name}, who teaches {self.subject}, casts a powerful spell!")

class SortingHat:
    HOUSES = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    def assign_house(self, person):
        house = random.choice(self.HOUSES)
        person.house = house
        print(f"{person.name}, you have been sorted into {house}!")


spell1 = Spell("Expelliarmus", "Disarms the opponent")
spell2 = Spell("Lumos", "Creates light at the wand's tip")
spell3 = Spell("Rictusempra", "Tickles the opponent and disarms them")
spell4 = Spell("Accio", "Summons objects to you")

student1 = Student("Harry Potter", 11, None, 1, [spell1, spell2])
student2 = Student("Luna Lovegood", 11, None, 1, [spell3, spell4])

sorting_hat = SortingHat()
sorting_hat.assign_house(student1)
sorting_hat.assign_house(student2)

student1.introduce()
student1.castSpell()

student2.introduce()
student2.castSpell()

professor1 = Professor("Severus Snape", 40, "Potions")
professor1.introduce()
professor1.castSpell()

professor2 = Professor("Albus Dumbledore", 90, "Headmaster Director")
professor2.introduce()
professor2.castSpell()
