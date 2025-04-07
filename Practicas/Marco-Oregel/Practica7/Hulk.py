from MarvelCharacter import MarvelCharacter
import random
class Hulk(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    
    def showPower(self):
        powers = ["HULK SMASH!","HULK WILL BREAK YOU!", "RAAAAGHHH!!","No Banner. Only Hulk"]
        power = random.choice(powers)
        print(power)

    def getAge(self):
        return super().getAge()
    
    def updateAge(self, newAge):
        return super().updateAge(newAge)
       