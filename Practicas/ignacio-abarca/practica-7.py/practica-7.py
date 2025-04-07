from abc import ABC, classmethod
class MarvelCharacter(ABC):
    classmethod
    def __init__(self, name, alias, universe, age ):
        self.name = name
        self.alias = alias
        self.universe = universe
        self._z_age = age
    
    def showPower(self):
        print(f"Con esto estás representando lo esencial que todo personaje Marvel tiene,ocultando los detalles específicos.")
    def getAge(self):
        print(f"su edad es {self.__age}")
    def updateAge(self, newAge):
        if newAge > 0:
            self.__age = newAge
            print(f"Edad actualizada correctamente")
        else:
            print("edad invalida, deve ser mayot a 0")
class IronMan(MarvelCharacter):

    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    def showPower(self):
        print(f"hola soy ironman, soy del universo de la mcu")
class SpiderMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    def showPower(self):
        print(f"hola soy spaiderman, soy del universo de la mcu")
class Thor(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    def showPower(self):
        print(f"hola soy Thor, soy del universo de la mcu")
class Holk(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    def showPower(self):
        print(f"hola soy holkr, soy del universo de la mcu")    
class CapitanAmercia(MarvelCharacter):
    def __init__(self, name, alias, universe, age):
        super().__init__(name, alias, universe, age)
    def showPower(self):
        print(f"hola soy cap, soy del universo de la mcu")  


def showHeroPower(character: MarvelCharacter):
    character.showPower()
tony = IronMan(name="Tony Stark", alias="Iron Man", universe="MCU", age=48)
showHeroPower(character=tony)
spider = SpiderMan (name="peter", alias="spideraman", universe="mcu", age=19)
showHeroPower(character=spider)
thor = Thor (name="elit", alias="thorr", universe="mcu", age=29)
showHeroPower(character=thor)
holk = Holk(name="brusbanner", alias="hulk",universe="mcu", age=43)
showHeroPower(character=holk)

steve = CapitanAmercia(name="capi", alias="capilan", universe="mcu", age=79)
showHeroPower(character=steve)




