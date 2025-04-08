class MarvelCharacter:
    def __init__(self, name: str, alias: str, universe: str, age: int, power: str):
        self.name = name
        self.alias = alias
        self.universe = universe
        self.power = power
        self.__age = age

    def getAge(self):
        return self.__age

    def showPower(self):
        print(f"{self.name}, better known as {self.alias}, is {self.__age} years old and his power is to '{self.power}'")

    def updateAge(self, newAge: int):
        if newAge > 0:
            self.__age = newAge
        else:
            print(f"Age must be greater than 0\n" "It was not possible to update the age because the requirements are not met")

class IronMan(MarvelCharacter):
    def showPower(self):
        return super().showPower()
    
class SpiderMan(MarvelCharacter):
    def showPower(self):
        return super().showPower()
    
class CaptainAmerica(MarvelCharacter):
    def showPower(self):
        return super().showPower()
    
class BlackWidow(MarvelCharacter):
    def showPower(self):
        return super().showPower()
    
class ScarletWitch(MarvelCharacter):
    def showPower(self):
        return super().showPower()
    
def showHeroPower(character: MarvelCharacter):
    character.showPower()

ironMan = IronMan("Tony Shark", "Iron Man", "MCU", 53, "Fly")
ironMan.updateAge(48)
showHeroPower(character = ironMan)

spiderMan = SpiderMan("Peter Parker", "Spider Man", "MCU", 25, "Spider - Sense")
showHeroPower(character = spiderMan)

captainAmerica = CaptainAmerica("Steve Rogers", "Captain America", "MCU", 30, "Indestructible shield")
captainAmerica.updateAge(-6)
showHeroPower(character = captainAmerica)

blackWidow = BlackWidow("Natasha Romanoff", "Black Widow", "MCU", 35, "Espionage")
showHeroPower(character = blackWidow)

scarletWitch = ScarletWitch("Wanda Maximoff", "Scarlet Witch", "MCU", 30, "Telekinesis")
scarletWitch.updateAge(32)
showHeroPower(character = scarletWitch)