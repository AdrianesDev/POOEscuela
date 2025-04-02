import random

class Spell:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def cast(self):
        print(f"!{self.name}! {self.description}")

class MagicPerson:
    def __init__(self, name: str, age: int, house: str = None):
        self.name = name
        self.age = age
        self.house = house

    def introduce(self):
        house_info = f"and I belong to {self.house} house" if self.house else "and I don't have a house assigned yet"
        print(f"My name is {self.name}, I'm {self.age} years old {house_info}.")

    def cast_spell(self):
        pass

class Student(MagicPerson):
    def __init__(self, name: str, age: int, yearsAtHogwarts: int, house: str = None):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = yearsAtHogwarts
        self.favoriteSpells = []

    def cast_spell(self):
        if not self.favoriteSpells:
            print(f"{self.name} doesn't know any spells yet.")
            return
        random_spell = random.choice(self.favoriteSpells)
        random_spell.cast()

class Professor(MagicPerson):
    def __init__(self, name: str, age: int, subject: str, house: str = None):
        super().__init__(name, age, house)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I am a professor of {self.subject}.")

    def cast_spell(self):
        print(f"Professor {self.name} performs an advanced {self.subject} spell!")

class SortingHat:
    def assignHouse(self, to):
        houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
        assigned_house = random.choice(houses)
        to.house = assigned_house
        print(f"{to.name}, you will be in... {assigned_house.upper()}!")
        return assigned_house


sorting_hat = SortingHat()

expelliarmus = Spell("Expelliarmus", "disarms your opponent")
lumos = Spell("Lumos", "lights up your wand")
wingardium_leviosa = Spell("Wingardium Leviosa", "makes objects levitate")
alohomora = Spell("Alohomora", "opens locked doors")

harry = Student("Harry Potter", 11, 1)
hermione = Student("Hermione Granger", 11, 1)
ron = Student("Ron Weasley", 11, 1)

harry.favoriteSpells.append(expelliarmus)
hermione.favoriteSpells.append(wingardium_leviosa)
ron.favoriteSpells.append(lumos)
ron.favoriteSpells.append(alohomora)

mcgonagall = Professor("Minerva McGonagall", 65, "Transfiguration")
snape = Professor("Severus Snape", 38, "Potions")

sorting_hat.assignHouse(harry)
sorting_hat.assignHouse(hermione)
sorting_hat.assignHouse(ron)
sorting_hat.assignHouse(mcgonagall)
sorting_hat.assignHouse(snape)

print("\n--- Introductions ---")
harry.introduce()
hermione.introduce()
ron.introduce()
mcgonagall.introduce()
snape.introduce()

print("\n--- Spells ---")
harry.cast_spell()
hermione.cast_spell()
ron.cast_spell()
mcgonagall.cast_spell()
snape.cast_spell()