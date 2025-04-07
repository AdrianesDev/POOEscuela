class MarvelCharacter:
    def __init__(self, name, alias, universe, age):
        self.name = name
        self.alias = alias
        self.universe = universe 
        self.__age = age

    def ShowPower(self):
        print(f"{self.name} has some power.")

    def getAge(self):
        return self.__age 
    
    def updateAge(self, newAge):
        if newAge > 0:
            self.__age = newAge
            print(f"Age is {self.__age} years.")
        else:
            print(f"Invalid age. Must be greater than 0.")

class CaptainAmerica(MarvelCharacter):
    def ShowPower(self):
        print(f"{self.alias} se chingo un electrolic militar. Ahora esta mamado.")

class SpiderMan(MarvelCharacter):
    def ShowPower(self):
        print(f"{self.alias} lo pico una araña radiactiva, casualmente no lo mato. Ahora es un trepa muros, curiosamente frabica su telaraña.")

class BlackPanter(MarvelCharacter):
    def ShowPower(self):
        print(f"{self.alias} gatito negro con garras de un mineral chido.")

class ScarletWitch(MarvelCharacter):
    def ShowPower(self):
        print(f"{self.alias} gracias a experimentos con una piedrita y a un librito, tiene el chamuco dentro.")

class AntMan(MarvelCharacter):
    def ShowPower(self):
        print(f"{self.alias} habla y se convierte en hormiga.")

def ShowHeroPower(character: MarvelCharacter):
        character.ShowPower()

Cap = CaptainAmerica("Steve Rogers", "Cap", "MCU", 99)
insect = SpiderMan("Peter Parcker", "insect", "MCU", 15)
tchalla = BlackPanter("King Tchalla", "Tchalla", "MCU", 52)
Wanda = ScarletWitch("Wanda Maximoff", "Wanda", "MCU", 34)
Scott = AntMan("Scott Lang", "Scott", "MCU", 54)

ShowHeroPower(Cap)
ShowHeroPower(insect)
ShowHeroPower(tchalla)
ShowHeroPower(Wanda)
ShowHeroPower(Scott)

print(f"{Cap.alias} tiene {Cap.getAge()} años.")
print(f"{insect.alias} tiene {insect.getAge()} años.")
print(f"{tchalla.alias} tiene {tchalla.getAge()} años.")
print(f"{Wanda.alias} tiene {Wanda.getAge()} años.")
print(f"{Scott.alias} tiene {Scott.getAge()} años.")