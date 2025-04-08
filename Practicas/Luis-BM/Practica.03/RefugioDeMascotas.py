class Pet:
    def __init__(self, name, type, age):
        self.name = name 
        self.type = type
        self.age = age
        self.isAdopted = False

    def description (self):
        status = "Adopted" if self.isAdopted else "Not adopted"
        print(f"{self.name} is a {self.type} that is {self.age} years old, it's {status}")

    def adopt(self):
         self.isAdopted = True

pet = Pet (name = "Firulais", type = "Dog", age = 2)
pet.description()
pet.adopt()
pet.description()

pet = Pet (name = "Elit", type = "Cat", age = 3)
pet.description()
pet.adopt()
pet.description()