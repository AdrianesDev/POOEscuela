from Mascota import Mascota
from Mascota import User

user = User("Marco")

mascota1 = Mascota("Firulais", "perro", 3)
mascota2 = Mascota("Felix", "gato", 1)

mascota1.description()
mascota2.description()

user.adoptar(mascota1)

mascota1.description()
mascota2.description()