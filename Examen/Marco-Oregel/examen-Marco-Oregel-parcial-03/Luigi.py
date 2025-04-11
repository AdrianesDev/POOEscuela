from Pilot import Pilot

class Luigi(Pilot):
    def __init__(self, name):
        super().__init__(name)
    
    def saludar(self):
        print(f"Mucho gusto yo me llamo {self.name}, soy el hermano de Mario!")