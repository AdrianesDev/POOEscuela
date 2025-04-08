from MarvelCharacter import MarvelCharacter
import random
class MoonKnight(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    
    def showPower(self):
        powers = ["I don't wear white so they can't see me... I wear it so they know I'm coming.","Random bullsh*t Go!","I am vengeance, I am the night, I am Mr. Knight!"]
        power = random.choice(powers)
        print(power)

    def getAge(self):
        return super().getAge()
    
    def updateAge(self, newAge):
        return super().updateAge(newAge)
       