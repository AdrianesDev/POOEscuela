from MarvelCharacter import MarvelCharacter
import random
class Thor(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    
    def showPower(self):
        powers = ["I am Thor, son of Odin!","For Asgard!", "Come to me, Mjölnir!","Feel the thunder of Mjölnir!"]
        power = random.choice(powers)
        print(power)

    def getAge(self):
        return super().getAge()
    
    def updateAge(self, newAge):
        return super().updateAge(newAge)
       