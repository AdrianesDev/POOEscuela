#include <iostream>
using namespace std;

class Corredor
{
public:
string nombre;
int velocidad;
void acelerar() {}
};

class Mario : public Corredor
{
public:
void acelerar()
{
  cout << "Mario acelera para ganar! 🏆 " << endl;
}
};

class Bowser : public Corredor
{
public:
void acelerar()
{
    cout << "Bowser acelera para atrapar a Mario! 😈 " << endl;
}
};

class Toad : public Corredor
{
private:
int cantidadDePlatanos = 3;
public:
void lanzarPlatanos()
{   
    if (cantidadDePlatanos > 0){
      cantidadDePlatanos-=1;
      cout << "Toad lanza un plátano! 🍌, Quedan "<< cantidadDePlatanos << endl;
    }else{
      cout << "Toad no tiene más plátanos! 😢" << endl;
    }
}
void recargarPlatanos()
{   
    cantidadDePlatanos = 3;
}
};

class Vehiculo
{
public:
string tipo;
void description() {}
};

class kart : public Vehiculo
{
public:
void description()
{
  cout << "El kart es muy veloz" << endl;
}
};

class Moto : public Vehiculo
{
public:
void description()
{    
  cout << "Es una moto muy veloz" << endl;
}
};

class Piloto
{
public:
void saludar() {}
};

class Luigi : public Piloto
{
public:
void saludar()
{
  cout << "¡Hola! Soy Luigi, el hermano de Mario. ¡Vamos a ganar! 🥇 " << endl;
}
};

class Yoshi : public Piloto
{
public:
void saludar()
{
  cout << "¡Hola! Soy Yoshi, el dinosaurio de Mario. ¡Vamos a ganar! 🦖 " << endl;
}
};

int main ()
{
    Mario mario; 
    mario.nombre = "Mario";
    mario.velocidad = 100;
    cout<< "El nombre del corredor es: " << mario.nombre << endl;
    cout<< "La velocidad de Mario es: " << mario.velocidad << "km/h"<< endl;
    mario.acelerar();
    cout<<""<<endl;
    Bowser bowser;
    bowser.nombre = "Bowser";
    bowser.velocidad = 96;
    cout<< "El nombre del corredor es: " << bowser.nombre << endl;
    cout<< "La velocidad de Bowser es: " << bowser.velocidad << "km/h"<< endl;
    bowser.acelerar();
    cout<<""<<endl;
    Toad toad;
    toad.lanzarPlatanos();
    cout<<""<<endl;
    toad.lanzarPlatanos();   
    cout<<""<<endl;
    toad.lanzarPlatanos();
    cout<<""<<endl;
    toad.lanzarPlatanos();
    cout<<""<<endl;
    toad.recargarPlatanos();
    toad.lanzarPlatanos();  
    cout<<""<<endl;
  
    kart kart;
    kart.tipo = "Kart";
    cout<<"Es un "<< kart.tipo <<endl;
    kart.description();
    cout<<""<<endl;

    Moto moto;
    moto.tipo = "Moto";
    cout<<"Es una "<< moto.tipo <<endl;
    moto.description();
    cout<<""<<endl;

    Luigi luigi;
    luigi.saludar();
    cout<<""<<endl;

    Yoshi yoshi;
    yoshi.saludar();
    cout<<""<<endl;

    return 0;
};