from abc import ABC
class Runner(ABC):
    def __init__(self,name,velocity):
        self.name = name
        self.velocity = velocity

    def accelerate():
        pass

class Mario(Runner):
    def __init__(self, name, velocity):
        super().__init__(name, velocity)
    
    def accelerate(self):
        print(f"{self.name} has increased speed with a mushroom to {self.velocity} Km")
    
class Bowser(Runner):
    def __init__(self, name, velocity):
        super().__init__(name, velocity)

    def accelerate(self):
        print(f"{self.name} has thrown a turtle shell to overtake Mario is going to {self.velocity} Km")
    
class Toad(Runner):
    def __init__(self):
        self.__amountofbananas = 3
    

    def throw_bananas(self):
        if self.__amountofbananas > 0:
            self.__amountofbananas -= 1
            print(f"Toad throws a banana you have left {self.__amountofbananas}")
        else:
            print(f"Toad doesn't have bananas")

    
    def recharge_bananas(self):
        self.__amountofbananas = 3
        print(f"Rechargin bananas: {self.__amountofbananas}")

    def get_amountofbananas(self):
        return self.__amountofbananas

class Vehicle():
    def __init__(self,type):
        self.type = type
    
    def description():
        print("This a generic text.")
        pass

class Kart(Vehicle):
    def __init__(self, type):
        super().__init__(type)
    
    def description(self):
        print(f"{self.type} has a peculiar design")

class Moto(Vehicle):
    def __init__(self, type):
        super().__init__(type)

    def description(self):
        print(f"{self.type} has an elegant design")
    
class Pilot():
    def __init__(self,name):
        self.name = name

    def say_hello():
        print("This a generic text.")
        pass

class Luigi(Pilot):
    def __init__(self, name):
        super().__init__(name)
    
    def say_hello(self):
        print(f"{self.name} greets you with concern")

class Yoshi(Pilot):
    def __init__(self, name):
        super().__init__(name)
    
    def say_hello(self):
        print(f"{self.name} greets you about to throw a shell at luigi")

    
luigi = Luigi("Luigi")
yoshi = Yoshi("Yoshi")
mario = Mario("Mario",17)
bowser = Bowser("Bowser",10)
toad = Toad()
kart = Kart("GO Kart")
moto = Moto("Moto")

toad.recharge_bananas()
moto.description()
kart.description()
toad.throw_bananas()
bowser.accelerate()
mario.accelerate()
luigi.say_hello()
yoshi.say_hello()


    



