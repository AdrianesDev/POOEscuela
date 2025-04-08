class Corredor:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
    
    def acelerar(self):
        pass

class Mario(Corredor):
    def acelerar(self):
        self.velocidad += 3
        return f"It's a me, Mario! Velocidad aumentada a {self.velocidad}"

class Bowser(Corredor):
    def acelerar(self):
        self.velocidad += 2
        return f"ROAAAR! Bowser aumenta su velocidad a {self.velocidad}"
    
class Toad:
    def __init__(self):
        self.__cantidadDePlatanos = 0
    
    def lanzarPlatano(self):
        if self.__cantidadDePlatanos > 0:
            self.__cantidadDePlatanos -= 1
            print(f"Toad lanza un plátano! Quedan {self.__cantidadDePlatanos}")
        else:
            print("No quedan platanos")   
    def recargarPlatanos(self):
        self.__cantidadDePlatanos = 3
        print(f"Plátanos recargados a {self.__cantidadDePlatanos}")

class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    def descripcion(self):
        return (f"Este es un vehículo de tipo {self.tipo}")

class Kart(Vehiculo):
    def __init__(self):
        super().__init__("Kart")   
    def descripcion(self):
        return (f"Un veloz kart de cuatro ruedas listo para la carrera!")

class Moto(Vehiculo):
    def __init__(self):
        super().__init__("Moto")
    def descripcion(self):
        return (f"Esta es una veloz moto lista para la carrera!")

class Piloto:
    def __init__(self, name):
        self.name = name
    
    def saludar(self):
        return (f"Hola, soy un piloto")
    
class Luigi(Piloto):
    def __init__(self):
        super().__init__("Luigi")       
    def saludar(self):
        return (f"Luigi! soy el numero uno! Ya-hoo!")
    
class Yoshi(Piloto):
    def __init__(self):
        super().__init__("Yoshi")       
    def saludar(self):
        return (f"Soy Yoshi! y soy el corredor mas rapido!")
    
if __name__ == "__main__":

    print("\n-----Ejercicio 1-----")
    mario = Mario("Mario", 10)
    bowser = Bowser("Bowser", 8)
    print(mario.acelerar())
    print(bowser.acelerar())

    print("\n-----Ejercicio 2-----")
    toad = Toad()

    toad.recargarPlatanos() 
    toad.lanzarPlatano()
    toad.lanzarPlatano()
    toad.lanzarPlatano()
    toad.lanzarPlatano()
    toad.recargarPlatanos()
    toad.lanzarPlatano()

    print("\n-----Ejercicio 3-----")

    kart = Kart()  
    moto = Moto()  
    print(kart.descripcion())
    print(moto.descripcion())  

    print("\n-----Ejercicio 4-----")

    luigi = Luigi()
    yoshi = Yoshi()
    pilotos = [luigi, yoshi]
    for piloto in pilotos:
        print(piloto.saludar())