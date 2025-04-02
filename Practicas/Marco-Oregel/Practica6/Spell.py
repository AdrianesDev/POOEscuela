class Spell:

    def __init__(self,name,description):
        self.name = name
        self.description = description

    def cast(self):
        print(f"{self.name}! {self.description}")
