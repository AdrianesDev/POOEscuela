class Pet:
    def __init__(self, name: str, type: str, age, isAdopted: bool = False):
        self.name = name
        self.type = type
        self.age = age
        self.isAdopted = isAdopted
    def description(self) -> str:
        status = "Adopted" if self.isAdopted else "Not adopted"
        return f"{self.name} is a {self.type} and is {self.age} years old. it's {status}"
    def adopt(self):
        if not self.isAdopted:
            self.isAdopted = True
            print(f"{self.name} has not been adopted.")
        else:
            print(f"{self.name} has already been adopted.")
            return True
    
pet = Pet(name = "Firulais", type = "Dog", age = 3, isAdopted = False)
print(pet.description())
pet.adopt()