class Runner:
    def __init__(self, name: str, velocidad: int):
        self.name = name 
        self.velocidad = velocidad

    def accelerate(self):
        pass 

class Mario(Runner):
   def accelerate(self):
       self.velocidad += 5
       print(f"WOW Mario acelero a {self.velocidad}")

class Bowser(Runner):
    def accelerate(self):
        self.velocidad += 7
        print(f"WOW Bowser acelero a {self.velocidad}")

class Toad:
    def __init__(self):

        self.__cantidadDePlatanos = 3

    def lanzarPlatano(self):
        if self.__cantidadDePlatanos > 0:
         self.__cantidadDePlatanos -= 1

         print(f"Toad lanza un plátano y quedan {self.__cantidadDePlatanos}")
        else:
          print(f"Ya no quedan platanos")

    def recargarPlatanos(self):
        self.__cantidadDePlatanos = 3
        print(f"Toad recargo platanos y tiene {self.__cantidadDePlatanos}")

class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def descripcion(self):
        return f"Este es un vehículo de tipo {self.tipo}"
    
class Kart (Vehiculo):
    def __init__(self):
        super().__init__("KART")
    
    def descripcion(self):
        return f"Este es un increible y veloz {self.tipo}"
    
class Moto (Vehiculo):
    def __init__(self):
        super().__init__("Moto")
    
    def descripcion(self):
        return f"Esta es una increible {self.tipo}"

class Piloto:
    def saludar(self):

        print(f"Saludan a lo lejos")

class Luigi(Piloto):

    def saludar(self):
        print(f"MAMA MIA")

class Yoshi(Piloto):
    def saludar(self):
        print(f"Hola soy Yoshi")

mario = Mario ("Mario", 5)
bowser = Bowser("Bowser" ,7)

print(f"{mario.name} tiene una velocidad de {mario.velocidad}")
mario.accelerate()
print(f"{mario.name} ahora tiene una velocidad de {mario.velocidad}")

print(f"{bowser.name} tiene una velocidad de {bowser.velocidad}")
bowser.accelerate()
print(f"{bowser.name} ahora tiene una velocidad de {bowser.velocidad}")

toad = Toad()

toad.lanzarPlatano()
toad.lanzarPlatano()
toad.lanzarPlatano()
toad.lanzarPlatano()
toad.recargarPlatanos()

kart = Kart()
moto = Moto()

print(kart.descripcion())
print(moto.descripcion())

luigi = Luigi()
yoshi = Yoshi()

luigi.saludar()
yoshi.saludar()



