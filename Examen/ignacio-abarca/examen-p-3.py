
class Corredor():
    def __init__(self, nombre: str, velocidad: int):
        self.name = str
        self.velocidad = int

    def acelerar(self):
        pass

class Mario(Corredor):
    def __init__(self, nombre, velocidad):
        super().__init__(nombre, velocidad)
    def acelerar(self):
        print(f"nunca me alcansaras bowser rata")
class Bowser(Corredor):
    def __init__(self, nombre, velocidad):
        super().__init__(nombre, velocidad)
    def acelerar(self):
        print(f"te estoy ganando mario, jaja")
class Toad(Corredor):
    def __init__(self, nombre, velocidad, cantidadDePlatanos = 3):
        super().__init__(nombre, velocidad)
        self.cantidadDePlatanos = cantidadDePlatanos

    def lanzarPratano(self):
        if self.cantidadDePlatanos > 0:
            self.cantidadDePlatanos -= 1
            print(f"¡Toad lanza un plátano! quedan {self.cantidadDePlatanos}")
        else:
            print(f"No quedan plátanos")

    def racargarPlatano(self):
        self.cantidadDePlatanos = 3
        print(f"Se llenaron los plátanos, tienes {self.cantidadDePlatanos}")

class Vehiculo:
    def __init__(self, tipo: str):
        self.tipo = str
    
    def descripcion(self):
        pass

class Kart(Vehiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
    def descripcion(self):
        print(f"kart le gana a a moto")

class Moto(Vehiculo):
    def __init__(self, tipo):
        super().__init__(tipo)
    def descripcion(self):
        print(f"moto le gana a kart")

class Piloto:
    def saludar(self):
        pass
class Luigi(Piloto):
    def saludar(self):
        print(f"les estoy ganando perros")\

class Yoshi(Piloto):
    def saludar(self):
        print(f"GG como siempre yoshi on top")


mario = Mario("Mario", 15)
bowser = Bowser("Bowser", 12)
toad = Toad("Toad", 10)

print(f"{mario.name} (velocidad: {mario.velocidad}): ")
mario.acelerar()
print(f"{bowser.name} (velocidad: {bowser.velocidad}):")
bowser.acelerar()
print(f"{toad.name} (velocidad: {toad.velocidad}), plátanos: {toad.cantidadDePlatanos}")
toad.lanzarPratano()
toad.lanzarPratano()
toad.lanzarPratano()
toad.lanzarPratano()
toad.racargarPlatano()
toad.lanzarPratano()

kart = Kart("Estándar")
moto = Moto("Deportiva")
kart.descripcion()
moto.descripcion()

luigi = Luigi()
yoshi = Yoshi()
luigi.saludar()
yoshi.saludar()
