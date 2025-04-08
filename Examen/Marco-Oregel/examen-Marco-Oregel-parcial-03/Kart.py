from Vehicle import Vehicle

class Kart(Vehicle):
    def __init__(self, color):
        super().__init__(color)


    def description(self):
         print(f"Carro de carreras de color {self.color}, es muy rapido!")