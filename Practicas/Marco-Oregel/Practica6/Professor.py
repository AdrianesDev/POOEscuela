from MagicPerson import MagicPerson

class Professor(MagicPerson):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject

    def castSpell(self):
      print(f"Soy el profesor {self.name} de la clase de {self.subject}, Petrificus Totalus!")