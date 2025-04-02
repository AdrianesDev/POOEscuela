class Mascota:

    def __init__(self,name,animal,age,):
        self.name = name
        self.animal = animal
        self.age = age
        self.isAdopted = False

    def description(self):
        if self.age == 1:
            print( f"- {self.name} es un {self.animal} de {self.age} año. Estado: {"Adoptado" if self.isAdopted else "No adoptado"}")
        else:
            print( f"- {self.name} es un {self.animal} de {self.age} años. Estado: {"Adoptado" if self.isAdopted else "No adoptado"}")
        



class User:
     def __init__(self,nombre):
          self.nombre = nombre
    
     def adoptar(self,mascota:Mascota):
        if not mascota.isAdopted:
             mascota.isAdopted= True
             print(f"{mascota.name} has been adopted by {self.nombre} successfully!")
    
    

        

