from MagicPerson import MagicPerson
import random

class Student(MagicPerson):
    def __init__(self, name, age, years, spells):
        super().__init__(name, age)
        self.years = years
        self.spells = spells
      
    
    def castSpell(self):
        spell = random.choice(self.spells)
        spell.cast()

    def introduce(self):
        print(f"Hola mi nombre es: {self.name}, tengo {self.age} años y estoy en la casa de {self.house}")
    
    
