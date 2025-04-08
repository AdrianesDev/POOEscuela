class Pet:
    def __init__(self, Name, Type, Age):
        self.name = Name 
        self.type = Type
        self.age = Age
        self.isAdopted = False

    def description(self):
        Status = "Adopt" if self.isAdopted else "Not Adopted"
        return f"{self.name} is a {self.type} and is {self.age} years old. Status: {Status}"

    def adopt(self):
        if self.isAdopted:
            self.isAdopted = True
            print(f"{self.name} has been adopted.")
        else:
            print(f"{self.name} has not been adopted.")
            return True
        
pet = Pet("Gabo", "Cat", 1)
print(pet.description()) 
pet.adopt()
pet = Pet("Chilo", "Cat", 3)
print(pet.description()) 
pet.adopt()
