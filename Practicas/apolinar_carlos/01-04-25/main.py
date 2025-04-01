import random


class Spell:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def cast(self):
        return f"¡{self.name}! {self.description}."
    


class MagicPerson:
    def __init__(self, name, age, house=None):
        self.name = name
        self.age = age
        self.house = house
    
    def introduce(self):
        house_info = f"from {self.house} house" if self.house else "not yet sorted"
        print(f"I'm {self.name}, I'm {self.age} years old and I'm {house_info}.")
    
    def castSpell(self):
        print(f"{self.name} makes a generic magical gesture.")

class Student(MagicPerson):
    def __init__(self, name, age, years_at_hogwarts, favorite_spells, house=None):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = years_at_hogwarts
        self.favoriteSpells = favorite_spells
    
    def castSpell(self):
        if self.favoriteSpells:
            spell = random.choice(self.favoriteSpells)
            print(f"{self.name} casts a spell: {spell.cast()}")
        else:
            print(f"{self.name} tries to cast a spell but doesn't know any.")




class Professor(MagicPerson):
    def __init__(self, name, age, subject, house=None):
        super().__init__(name, age, house)
        self.subject = subject
    
    def castSpell(self):
        print(f"{self.name}, {self.subject} professor, casts a powerful spell: ¡{self.subject} Maxima!")



class SortingHat:
    HOUSES = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    
    @classmethod
    def assignHouse(cls, person):
        house = random.choice(cls.HOUSES)
        person.house = house
        print(f"¡{person.name}, you belong to... {house.upper()}!")
        return house
    

    

spells = [
    Spell("Expelliarmus", "disarms your opponent"),
    Spell("Lumos", "lights up your wand"),
    Spell("Nox", "turns off the light from your wand"),
    Spell("Wingardium Leviosa", "makes objects levitate"),
    Spell("Alohomora", "opens locked doors"),
    Spell("Petrificus Totalus", "freezes the opponent completely"),
    Spell("Stupefy", "knocks out or stuns the opponent"),
    Spell("Accio", "summons objects to you"),
    Spell("Protego", "casts a shield to block spells"),
    Spell("Rictusempra", "tickles the opponent and disarms them")
]


harry = Student("Harry Potter", 11, 1, [spells[0], spells[5], spells[7]])
hermione = Student("Hermione Granger", 11, 1, [spells[3], spells[4], spells[8]])
ron = Student("Ron Weasley", 11, 1, [spells[0], spells[3], spells[9]])
draco = Student("Draco Malfoy", 11, 1, [spells[0], spells[5], spells[6]])
luna = Student("Luna Lovegood", 11, 1, [spells[2], spells[3], spells[7]])
neville = Student("Neville Longbottom", 11, 1, [spells[3], spells[5], spells[8]])

dumbledore = Professor("Albus Dumbledore", 115, "Headmaster")
mcgonagall = Professor("Minerva McGonagall", 60, "Transfiguration")
snape = Professor("Severus Snape", 38, "Potions")
lupin = Professor("Remus Lupin", 34, "Defense Against the Dark Arts")
flitwick = Professor("Filius Flitwick", 45, "Charms")
trelawney = Professor("Sybill Trelawney", 50, "Divination")
hagrid = Professor("Rubeus Hagrid", 45, "Care of Magical Creatures")

SortingHat.assignHouse(harry)
SortingHat.assignHouse(hermione)
SortingHat.assignHouse(ron)
SortingHat.assignHouse(draco)
SortingHat.assignHouse(luna)
SortingHat.assignHouse(neville)

SortingHat.assignHouse(dumbledore)
SortingHat.assignHouse(mcgonagall)
SortingHat.assignHouse(snape)
SortingHat.assignHouse(lupin)
SortingHat.assignHouse(flitwick)
SortingHat.assignHouse(trelawney)
SortingHat.assignHouse(hagrid)

print("Introductions")
harry.introduce()
hermione.introduce()
dumbledore.introduce()
snape.introduce()

print("Spell Casting")
harry.castSpell()
hermione.castSpell()
ron.castSpell()
dumbledore.castSpell()
snape.castSpell()