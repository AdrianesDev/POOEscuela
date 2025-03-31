class Pet:
    def __init__(self, name: str, animal: str, age: int, adopted: bool):
        self.name = name
        self.animal = animal
        self.age = age
        self.adopted = False

    def description(self):
        print(f"{self.name} es un {self.animal} de {self.age} años. Adoptado: {self.adopted}")

    def adopt(self):
        if not self.adopted:
            self.adopted = True
            self.description()
    
rabbit = Pet('Pipi', 'conejo', 2, False)
dog = Pet('Doki', 'perro', 4, False)

rabbit.description()
rabbit.adopt()

dog.description()
dog.adopt()