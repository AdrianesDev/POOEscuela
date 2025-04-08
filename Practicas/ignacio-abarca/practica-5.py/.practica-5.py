class Pet:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
        self.is_adopted = False


    def is_adopted_status(self):
        if self.is_adopted:
            print(f"{self.name} is adopted")
            return
        else:
            print(f"{self.name} is available")
            return
    def adopt(self):
        self.is_adopted = True
        print(f"Do you want to adopt: {self.name}")


    def description(self):
        status = "adopted" if self.is_adopted else "not adopted"
        print(f"{self.name} is a {self.type} of {self.age} years old.")

pet1 = Pet("Firulais", "Dog", 3)
pet2 = Pet("Michi", "Cat", 2)
pet3 = Pet("Luis", "Iguana", 19 )

print("\n[INFO] Checking and updating adoption status...\n")
pet1.description()

pet1.adopt()
pet1.is_adopted_status()
print("-" * 20)

print("\n[INFO] Checking and updating adoption status...\n")

pet2.description()
pet2.is_adopted_status()
pet2.adopt()
pet2.is_adopted_status()


