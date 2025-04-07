from abc import ABC, abstractmethod
class MarvelCharacter:
    def __init__(self, name, alias, universe):
        self.name = name 
        self.alias = alias 
        self.universe = universe
        self.__age = 0

    def showPower(self):
        print(f"{self.name} has powers")

    def getAge(self):
        return self.__age
    
    def updateAge(self, newAge):
        if newAge > 0:
            self.__age = newAge
        else:
            print("Age must be greater than 0")

class IronMan(MarvelCharacter):
    def showPower(self):
        print(f"{self.name} alias {self.alias} of {self.universe} uses his armor")

class SpiderMan(MarvelCharacter):
    def showPower(self):
        print(f"{self.name} alias {self.alias} of {self.universe} uses his webs")


def showHeroPower(character):
    character.showPower()

tony = IronMan (name = "Tony Stark", alias = "Iron Man", universe = "MCU")
tony.updateAge(newAge = 50)
print(f"{tony.name} is {tony.getAge()} years old")

peter = SpiderMan(name = "Peter Parker", alias = "SpiderMan", universe = "MCU")
peter.updateAge(newAge = 16)
print(f"{peter.name} is {peter.getAge()} years old")

showHeroPower(tony)
showHeroPower(peter)