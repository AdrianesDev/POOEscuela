from Racer import Racer

class Bowser(Racer):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    
    def acelerar(self):
      if self.speed == "rapida":
            self.speed = "muy rapida"
            print(f"Raaah! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
      elif self.speed == "lenta":
            self.speed = "rapida"
            print(f"Yea! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
      else:
            print("Grrr! El vehiculo se sobrecalento")

    