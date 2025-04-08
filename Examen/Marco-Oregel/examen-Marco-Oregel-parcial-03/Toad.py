from Racer import Racer

class Toad(Racer):
    def __init__(self, name, speed,bananas=3):
        super().__init__(name, speed)
        self._bananas = bananas
    
    def acelerar(self):
        if self.speed == "rapida":
            self.speed = "muy rapida"
            print(f"Wahoo! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
        elif self.speed == "lenta":
            self.speed = "rapida"
            print(f"Yay! {self.name} ha acelerado! su velocidad ahora es {self.speed}")
        else:
            print("Oh no! El vehiculo se sobrecalento")

    def throwBanana(self):
        self._bananas = self._bananas - 1
        if self._bananas > 1 or self._bananas == 0 :
            print(f"{self.name} lanza una banana! Le quedan {self._bananas} bananas")
        elif self._bananas == 1:
            print(f"{self.name} lanza una banana! Le queda {self._bananas} banana")
        else:
            print("Ya no te quedan mas bananas, recarga para poder lanzar mas.")

    def reloadBanana(self):
        self._bananas = 3
        print(f"{self.name} ha recargado sus bananas, tienes 3 denuevo!")

