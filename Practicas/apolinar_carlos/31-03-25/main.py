class Mascota():
    def __init__(self,nombre,tipo,edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.estaAdoptado = False

    def descripcion(self):
        print(f"{self.nombre} es un {self.tipo} de {self.edad} años. Estado: {self.estaAdoptado}")

    def adoptar(self):
        self.estaAdoptado = True

mi_mascota = Mascota("Max" , "Perro" , 2)

mi_mascota.descripcion()
mi_mascota.adoptar()
mi_mascota.descripcion()
