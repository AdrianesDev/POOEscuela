from MarvelCharacter import MarvelCharacter
from Ironman import Ironman
from Spiderman import Spiderman
from Hulk import Hulk
from Thor import Thor 
from MoonKnight import MoonKnight

def showHeroPower(character: MarvelCharacter):
    character.showPower()



Tony = Ironman("Tony Stark","Ironman","MCU",30)
Peter = Spiderman("Peter Parker","Spiderman","MCU",15)
thor = Thor("Thor","Thor","MCU",1000)
Bruce = Hulk("Bruce Banner","Hulk","MCU",35)
Mark = MoonKnight("Mark Spector", "Moonknight", "MCU", 28)


print("-" * 45)

print(Tony.getAge())

Tony.updateAge(40)

print(Tony.getAge())

Tony.showPower()

showHeroPower(character=Tony)

print("-" * 45)

print(Peter.getAge())
Peter.showPower()
showHeroPower(character=Peter)

print("-" * 45)

thor.updateAge(1500)
print(thor.getAge())
thor.showPower()
showHeroPower(character=thor)

print("-" * 45)

print(Mark.getAge())
Mark.showPower()
showHeroPower(character=Mark)

print("-" * 45)

print(Bruce.getAge())
Bruce.showPower()
showHeroPower(character=Bruce)
