from typing import Protocol

class RoleProtocol(Protocol):

    def __init__(self,name):
        self._name = name
       
    
    def loginProcess(self):
        print(f"Se ha iniciado sesion exitosamente, Bienvenido {self._name}!")