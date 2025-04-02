import random

class Spell:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def cast(self):
        return f"¡{self.name}!, {self.description}"

class MagicPerson:
    def __init__(self, name: str, age: int, house = None):
        self.name = name
        self.age = age
        self.house = house

    def introduce(self):
        print(f"{self.name} you are {self.age} years old, and you belong to {self.house}")

    def castSpell(self):
        pass

class Student(MagicPerson):
    def __init__(self, name, age, yearsAtHogwarts: int, favoriteSpells = None, house = None):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = yearsAtHogwarts
        self.favoriteSpells = favoriteSpells

        self.spell = [
            Spell("Expelliarmus", "disarms your opponent"),
            Spell("Lumos", "lights up your wand"),
            Spell("Nox", "turns off the light from your wand"),
            Spell("Wingardium Leviosa", "makes objects levitate"),
            Spell("Alohomora", "opens locked doors"),
            Spell("Petrificus Totalus", "freezes the opponent completely"),
            Spell("Stupefy", "knocks out or stuns the opponent"),
            Spell("Accio", "summons objects to you"),
        ]

    def castSpell(self):
        randomSpell = random.choice(self.spell)
        print(f"{self.name} you have cast the {randomSpell.cast()} spell")

class Professor(MagicPerson):
    def __init__(self, name, age, subject: str, house = None):
        super().__init__(name, age, house)
        self.subject = subject

    def castSpell(self):
        print(f"The teacher {self.name} cast a {self.subject} spell")

class SortingHat:
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    @staticmethod
    def assignHouse(self):
        assignHouse = random.choice(SortingHat.houses)
        self.house = assignHouse
        print(f"{self.name}, you will be from...{assignHouse.upper()}!")


harry = Student("Harry Potter", 11, 6)

SortingHat.assignHouse(harry)
harry.introduce()
harry.castSpell()
print("")

hermione = Student("Hermione Granger", 11, 5)

SortingHat.assignHouse(hermione)
hermione.introduce()
hermione.castSpell()
print("")

severus = Professor("Severus Snape", 31, "Potions")

severus.castSpell()

remus = Professor("Remus Lupin", 31, "Defense Against the Dark Arts")

remus.castSpell()