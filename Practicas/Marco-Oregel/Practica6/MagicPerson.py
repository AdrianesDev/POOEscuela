class MagicPerson:

    def __init__(self,name,age, house = None):
        self.name = name
        self.age = age
        self.house = house

    def castSpell(self):
        return "Abracadabra!"
    
    def introduce(self):
        chosenHouse = f" y soy de la casa {self.house}" if self.house else " "
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años{chosenHouse}.")