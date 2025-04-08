import random

class Spell:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def cast(self):
        print(f"¡{self.name}! {self.description}")

class MagicPerson:
    def __init__(self, name, age, house=None):
        self.name = name
        self.age = age
        self.house = house

    def introduce(self):
        print(f"I am {self.name}, I am {self.age} years old and I belong to {self.house}.")

    def CastSpell(self):
        print(f"{self.name} attempts to cast a spell... But it's not clear which one.")

class Student(MagicPerson):
    def __init__(self, name, age, yearsAtHogwarts, house=None):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = yearsAtHogwarts
        self.favoriteSpells = []

    def addFavoriteSpell(self, spell):
        self.favoriteSpells.append(spell)

    def CastSpell(self):
        if self.favoriteSpells:
            spell = random.choice(self.favoriteSpells)
            spell.cast()
        else: 
            print(f"{self.name} has no favorite spell yet.")

class Professor(MagicPerson):
    def __init__(self, name, age, subject, house=None):
        super().__init__(name, age, house)
        self.subject = subject

    def CastSpell(self):
        print(f"{self.name}, {self.subject}'s teacher, casts a masterful spell.")

class SortingHat:
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    @staticmethod
    def assignHouse(person):
        house = random.choice(SortingHat.houses)
        person.house = house
        print(f"¡{person.name}, serás de... {house.upper()}!")
        
spell1 = Spell("Nox", "Turns off the light from your wand.")
spell2 = Spell("Petrificus Totalus", "Freezes the opponent completely.")
spell3 = Spell("Rictusempra", "Tickles the opponent and disarms them.")

Hermione = Student("Hermione Granger", 11, 1)
Hermione.addFavoriteSpell(spell1)
Hermione.addFavoriteSpell(spell2)

SortingHat.assignHouse(Hermione)
Hermione.introduce()
Hermione.CastSpell()

snape = Professor("Severus Snape", 38, "Potions", "Mysterious")
snape.introduce()
snape.CastSpell()