#Abstracción
class Corredor:
    def __init__(self, nombre: str, velocidad: int):
        self.nombre = nombre
        self.velocidad = velocidad

    def acelerar(self):
        pass

class Mario(Corredor):
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.nombre} está acelerando. Velocidad actual: {self.velocidad}")

class Bowser(Corredor):
    def acelerar(self):
        self.velocidad += 5
        print(f"{self.nombre} está acelerando. Velocidad actual: {self.velocidad}")

#Encapsulamiento
class Toad:
    def __init__(self, cantidadDePlatanos: int = 3):
        self.__cantidadDePlatanos = cantidadDePlatanos

    def getCantidadDePlatanos(self):
        return self.__cantidadDePlatanos

    def lanzarPlatano(self):
        if self.__cantidadDePlatanos > 0:
            self.__cantidadDePlatanos -= 1
            print("¡Plátano lanzado!")
            print(f"Plátanos restantes: {self.__cantidadDePlatanos}")
            return True
        else:
            print("¡No hay plátanos!")
            return False

    def recargarPlatanos(self):
        self.__cantidadDePlatanos = 3
        print("Plátanos recargados. ¡Listo para lanzar!")

#Herencia
class Vehiculo:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def descripcion(self):
        pass

class Kart(Vehiculo):
    def descripcion(self):
        print(f"Este es un {self.tipo} de Mario Kart")

class Moto(Vehiculo):
    def descripcion(self):
        print(f"Este es una {self.tipo} de Mario Kart")

#Polimorfismo
class Piloto:
    def saludar(self):
        pass

class Luigi(Piloto):
    def saludar(self):
        print("¡Hola, soy Luigi!")

class Yoshi(Piloto):
    def saludar(self):
        print("¡Hola, soy Yoshi!")

#Instancias
mario = Mario("Mario", 10)
mario.acelerar()

toad = Toad()
toad.lanzarPlatano()
toad.lanzarPlatano()
toad.lanzarPlatano()
toad.lanzarPlatano()
toad.recargarPlatanos()
toad.lanzarPlatano()

kart = Kart("Kart")
kart.descripcion()

bowser = Bowser("Bowser", 40)
bowser.acelerar()

luigi = Luigi()
luigi.saludar()

yoshi = Yoshi()
yoshi.saludar()