from MarvelCharacter import MarvelCharacter
import random
class Ironman(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    
    def showPower(self):
        powers = ["JARVIS, Engage heads-up display!","Power up the suit!","I am Iron Man.", "Jarvis, drop my needle"]
        power = random.choice(powers)
        print(power)

    def getAge(self):
        return super().getAge()
    
    def updateAge(self, newAge):
        return super().updateAge(newAge)
       