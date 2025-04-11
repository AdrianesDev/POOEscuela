from Toad import Toad
from Luigi import Luigi
from Bowser import Bowser
from Mario import Mario 
from Yoshi import Yoshi
from Kart import Kart
from Motocycle import Motocycle

toad = Toad("Toad","rapida")
bowser = Bowser("Bowser","lenta")
mario = Mario("Mario","muy rapida")
kart = Kart("rojo")
moto = Motocycle("verde")
luigi = Luigi("Luigi")
yoshi = Yoshi("Yoshi")

print("-"*30)
toad.acelerar()

toad.throwBanana()

toad.reloadBanana()

toad.throwBanana()
toad.throwBanana()
toad.throwBanana()
toad.throwBanana()
toad.reloadBanana()

print("-" *30)

bowser.acelerar()
mario.acelerar()

print("-"* 30)

moto.description()
kart.description()

print("-"*30)

luigi.saludar()
yoshi.saludar()




