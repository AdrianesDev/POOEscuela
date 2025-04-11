from Pilot import Pilot

class Yoshi(Pilot):
    def __init__(self, name):
        super().__init__(name)
    
    def saludar(self):
        print(f"{self.name}: YOOOSHII!")