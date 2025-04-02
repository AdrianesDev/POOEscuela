import random
from Student import Student
from MagicPerson import MagicPerson

class SortingHat:
    def __init__(self):
        pass

    def assignHouse(self, student):
        houses = ["Gryffindor","Slytherin","Ravenclaw", "Hufflepuff"]
        house = random.choice(houses)
        student.house = house
        print(f"{student.name}, seras de... {house}!")


    
    