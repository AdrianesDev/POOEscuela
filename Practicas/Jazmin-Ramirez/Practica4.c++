#include <iostream>
#include <string>

using namespace std;

class Mascota {
private:
    string nombre;
    string tipo;
    int edad;
    bool estaAdoptado;

public:
    Mascota(string _nombre, string _tipo, int _edad)
        : nombre(_nombre), tipo(_tipo), edad(_edad), estaAdoptado(false) {}

    string descripcion() const {
        return nombre + " es un " + tipo + " de " + to_string(edad) + " años. Estado: " + 
               (estaAdoptado ? "Adoptado." : "No adoptado.");
    }

    void adoptar() {
        estaAdoptado = true;
    }
};

int main() {
    Mascota mascota1("Firulais", "Perro", 3);
    Mascota mascota2("Max", "Gato", 2);

    cout << mascota1.descripcion() << endl;

    mascota1.adoptar();
    cout << mascota1.descripcion() << endl;

    cout << mascota2.descripcion() << endl;

    return 0;
};