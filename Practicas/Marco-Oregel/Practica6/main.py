from MagicPerson import MagicPerson
from Student import Student
from SortingHat import SortingHat
from Spell import Spell
from Professor import Professor
import random

spell1 = Spell("Expelliarmus", "desarma al oponente.")
spell2 = Spell("Nox", "Apaga la luz de tu varita")
spell3 = Spell("Wingardium Leviosa", "Hace levitar objetos")
spell4 = Spell("Alohomora","Abre puertas cerradas con seguro")
spell5 = Spell("Petrificus Totalus","Inmoviliza al oponente completamente")
spell6 = Spell("Stupefy","Aturde al oponente")
spell7 = Spell("Accio","Te añade algun objeto")
spell8 = Spell("Protego", "Invoca un escudo que bloquea hechizos")
spell9 = Spell("Rictusempra","Hace cosquillas al oponente y lo desarma")


student1 = Student("Harry Potter", 11, 1,[spell1,spell2])
student2 = Student("Hermione Granger",11,1,[spell7,spell4,spell5])
student3 = Student("Ron weasley",11,1,[spell1,spell3])

professor1 = Professor("Sybill Trelawney",40, "Divinidad")

hat = SortingHat()

hat.assignHouse(student1)

student1.introduce()
student1.castSpell()
print("-"*50)
hat.assignHouse(student2)

student2.introduce()
student2.castSpell()
print("-"*50)
hat.assignHouse(student3)

student3.introduce()
student3.castSpell()
print("-"*50)

professor1.castSpell()