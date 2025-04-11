from Vehicle import Vehicle

class Motocycle(Vehicle):
    def __init__(self, color):
        super().__init__(color)


    def description(self):
        print(f"Motocicleta de color {self.color}, muy buena para hacer trucos!")