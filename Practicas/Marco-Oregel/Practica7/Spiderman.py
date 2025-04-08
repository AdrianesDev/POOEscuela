from MarvelCharacter import MarvelCharacter
import random
class Spiderman(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    
    def showPower(self):
        powers = ["Time to swing","Come on, Spidey-sense, don’t fail me now!","Web-shooters locked and loaded!", "Web to the ceiling, kick to the face!"]
        power = random.choice(powers)
        print(power)

    def getAge(self):
        return super().getAge()
    
    def updateAge(self, newAge):
        return super().updateAge(newAge)
       