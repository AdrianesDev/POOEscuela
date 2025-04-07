from typing import Protocol

class MarvelCharacter(Protocol):

    def __init__(self,name,alias,universe,age):
        self.name = name
        self.alias = alias
        self.universe = universe
        self._age = age
        

    def showPower(self):
        print(f"Pow,Boom,Kapow!")


    def getAge(self):
        return f"{self.name} is {self._age} years old"
    
    def updateAge(self, newAge):
        if self._age > 0:
            self._age = newAge
            print("Age has been updated!")
        else:
            print("Age must be greater than 0")