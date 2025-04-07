class MarvelCharacter:
    def __init__(self, name, alias, universe):
        self.name = name
        self.alias = alias
        self.universe = universe
        self.__age = 0

    def showPower(self):
        print(f"I am {self.name} and my superpowers are.")
        print(f"Age: {self.getAge()} years old")

    def getAge(self):
        return self.__age

    def updateAge(self, newAge):
        if newAge > 0:
            self.__age = newAge

class IronMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age = 0):
        super().__init__(name, alias, universe)
        self.updateAge(age)

    def showPower(self):
        super().showPower()
        print("I am IronMan and my superpowers are: I'm rich.")

class SpiderMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age = 0):
        super().__init__(name, alias, universe)
        self.updateAge(age)

    def showPower(self):
        super().showPower()
        print("I am SpiderMan and I have arachnid powers.")

class CaptainAmerica(MarvelCharacter):
    def __init__(self, name, alias, universe, age = 0):
        super().__init__(name, alias, universe)
        self.updateAge(age)

    def showPower(self):
        super().showPower()
        print("I am Captain America and I have Super Strength.")

class AntMan(MarvelCharacter):
    def __init__(self, name, alias, universe, age = 0):
        super().__init__(name, alias, universe)
        self.updateAge(age)

    def showPower(self):
        super().showPower()
        print("I am AntMan and I have ant powers.")

class DoctorStrange(MarvelCharacter):
    def __init__(self, name, alias, universe, age = 0):
        super().__init__(name, alias, universe)
        self.updateAge(age)

    def showPower(self):
        super().showPower()
        print("I am Doctor Strange and I have magic powers.")

def ShowHeroPowers(character: MarvelCharacter):
    character.showPower()
    print("-" * 30)

print("--Introduction--")
tony = IronMan(name="Tony Stark", alias="IronMan", universe="MCU", age=48)
peter = SpiderMan(name="Peter Parker", alias="Spiderman", universe="MCU", age=18)
steve = CaptainAmerica(name="Steve Rogers", alias="Captain America", universe="MCU", age=34)
scott = AntMan(name="Scott Lang", alias="AntMan", universe="MCU", age=30)
stephen = DoctorStrange(name="Stephen Strange", alias="Doctor Strange", universe="MCU", age=37)

ShowHeroPowers(tony)
ShowHeroPowers(peter)
ShowHeroPowers(steve)
ShowHeroPowers(scott)
ShowHeroPowers(stephen)




    