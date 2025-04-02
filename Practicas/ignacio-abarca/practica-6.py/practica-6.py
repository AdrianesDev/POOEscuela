import random
random_list = [random.randint(1, 4) for _ in range(10)]

class Spell:
    def __init__(self, name, descripcion):
        self.name = name
        self.descripcion = descripcion

    def cast(self):
        print(f"{self.name}: {self.descripcion}")

class MagicPerson:
    def __init__(self, name: str, age: int, house: str):
        self.name = name
        self.age = age
        self.house = house
        self.random = random.choice(random_list) 
    def introduce(self):
        print(f"Nombre: {self.name}, Edad: {self.age}, Casa: {self.house}")

    def castSpell(self):
        print(f"{self.name} lanza un hechizo genérico.")


class Student(MagicPerson):
    def __init__(self, name: str, age: int, house: str, yearsAtHogwarts: int, favoriteSpells: list):
        super().__init__(name, age, house)
        self.yearsAtHogwarts = yearsAtHogwarts
        self.favoriteSpells = favoriteSpells

    def castSpell(self):
        if self.favoriteSpells:
            spell = random.choice(self.favoriteSpells) 
            spell.cast()
        else:
            print(f"{self.name} no tiene hechizos favoritos.")

class Professor(MagicPerson):
    def __init__(self, name: str, age: int, house: str, subject: str):
        super().__init__(name, age, house)
        self.subject = subject

    def castSpell(self):
        print(f"El profesor {self.name} usa un hechizo especial en la materia {self.subject}.")

class SortingHat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @staticmethod
    def assignHouse():
        return random.choice(SortingHat.houses)  
spell1 = Spell("Expelliarmus", "Desarma al oponente")
spell2 = Spell("Lumos", "Ilumina la varita")

student = Student("Harry", 11, SortingHat.assignHouse(), 1, [spell1, spell2])
student.introduce()
student.castSpell()

professor = Professor("Snape", 50, "Slytherin", "Pociones")
professor.introduce()
professor.castSpell()



        

