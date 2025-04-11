from Racer import Racer

class Mario(Racer):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def acelerar(self):
        if self.speed == "rapida":
            self.speed = "muy rapida"
            print(f"Woo-hoo! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
        elif self.speed == "lenta":
            self.speed = "rapida"
            print(f"Let's GO! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
        else:
            print(f"Mama mia! El vehiculo se sobrecalento, {self.name} ha retrocedido un poco")
