from abc import ABC, abstractmethod
class MarvelCharacter(ABC):
    def __init__(self,name,alias,universe,age):
        self.name = name
        self.alias = alias
        self.universe = universe
        self._age = age
    
    def get_age(self):
        return self._age
    
    def update_age(self, newAge):
        if newAge > 0:
            self._age = newAge
        else:
            print("The age must be greater than 0.")
    
    def show_power(self):
        print("This is a SuperHeroes.")
    

class IronMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    
    def show_power(self):
        print(f"I'm {self.name}, but you can call me {self.alias}, i live in a mansion, my age is {self._age} and my universe is: {self.universe}.")


class SpiderMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)

    def show_power(self):
        print(f"Hi, I'm {self.name}, everyone knows me as {self.alias}, i save the evil of the New York city, i have {self._age} years old, and i'm from {self.universe}.")

def show_hero_power(character: MarvelCharacter):
    character.show_power()

tony = IronMan("Tony Stark","Iron Man","MCU",48)
parker = SpiderMan("Peter Parker","Spider-Man","MCU",17)

show_hero_power(character=tony)
show_hero_power(character=parker)
