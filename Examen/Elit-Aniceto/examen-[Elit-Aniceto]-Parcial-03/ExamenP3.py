class Corredor:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def acelerar(self):
        pass

class Mario(Corredor):
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.nombre} corre a {self.velocidad}. Anomos recio.")

class Bowser(Corredor):
    def acelerar(self):
        self.velocidad += 8
        print(f"{self.nombre} corre a {self.velocidad}. Con el pendiente de dar levanton al fontanero.")

class Toad(Corredor):
    def __init__(self):
        self.__cantidadDePlatanos = 3 

    def lanzarPlatano(self):
        if self.__cantidadDePlatanos > 0:
            self.__cantidadDePlatanos -= 1
            print(f"¡Lanzaste un plátano! Quedan:"), self.__cantidadDePlatanos
        else:
            print(f"¡No te quedan plátanos! Recarga para seguir lanzando.")

    def recargarPlatanos(self):
        self.__cantidadDePlatanos = 3
        print(f"Plátanos recargados. Tienes:"), self.__cantidadDePlatanos

class Vehiculo:
    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

class Kart(Vehiculo):
    def __init__(self):
        self.descripcion
        print(f"{self.descripcion} go kart de los chidos.")

class Moto(Vehiculo):
    def __init__(self):
        self.descripcion
        print(f"{self.descripcion} una mortalika.")

class Piloto:
    def saludar(self):
        print(f"hi, and good bye")

class Luigi(Piloto):
    def saludar(self):
        print(f"Mario donde estas?.")

class Yoshi(Piloto):
    def saludar(self):
        print(f"yoshiiiiiiii")

mario = Mario("Mario", 20)
bowser = Bowser("Bowser", 15)

toad = Toad()
toad.lanzarPlatano()

toad.recargarPlatanos()