#include <iostream>
using namespace std;

class MarvelCharacter
{
private:
int age;

public:
string name;
string alias;
string universe;

void showpower() {}

void getAge() {
    cout << "Edad actual: " << age << " años" << endl;
}

void updateAge(int newAge) {
    if (newAge > 0) {
        age = newAge;
        cout << "Edad actualizada con éxito" << endl;
    } else {
        cout << "Edad no válida. La edad debe ser mayor que 0" << endl;
    }
}
};

class SpiderMan : public MarvelCharacter
{
public:
void showpower() {
    cout << "Este personaje tiene la habilidad de trepar paredes!" << endl;
}
};

class IronMan : public MarvelCharacter{
public:
void showpower() {
    cout << "Este personaje tiene un traje de alta tecnología!" << endl;
}
};

class BrujaEscarlata : public MarvelCharacter{
public:
void showpower() {
    cout << "Este personaje tiene la habilidad de volar, lanzar rayos y bolas de energía!" << endl;
}
};

class BlackWidow : public MarvelCharacter{
public:
void showpower() {
    cout << "Este personajes es muy fuerte y muy veloz" << endl;
}
};

class Hulk : public MarvelCharacter{
public:
void showpower() {
    cout << "Este personaje tiene la habilidad de aumentar su fuerza!" << endl;
}
};

void showHeroPower(MarvelCharacter& character) {
    character.showpower();
}

int main(){
    SpiderMan spiderman;
  
    spiderman.name = "Peter Parker";
    spiderman.alias = "Spider-Man";
    spiderman.universe = "MCU";
  
    cout << "Nombre: " << spiderman.name << endl;
    cout << "Alias: " << spiderman.alias << endl;
    cout << "Universo: " << spiderman.universe << endl;
  
    spiderman.updateAge(20);
    spiderman.getAge();
    spiderman.showpower();
  
    showHeroPower(spiderman);

    cout << "------------------------------------------" << endl;
  
    IronMan ironman;
  
    ironman.name = "Tony Stark";  
    ironman.alias = "Iron Man";
    ironman.universe = "MCU";
  
    cout << "Nombre: " << ironman.name << endl;
    cout << "Alias: " << ironman.alias << endl;
    cout << "Universo: " << ironman.universe << endl;
  
    ironman.updateAge(45);
    ironman.getAge();
    ironman.showpower();
  
    showHeroPower(ironman);
  
    cout << "------------------------------------------" << endl;

    BlackWidow blackwidow;

    blackwidow.name = "Natasha Romanoff";
    blackwidow.alias = "Black Widow";
    blackwidow.universe = "MCU";

    cout << "Nombre: " << blackwidow.name << endl;
    cout << "Alias: " << blackwidow.alias << endl;
    cout << "Universo: " << blackwidow.universe << endl;
  
    blackwidow.updateAge(35);  
    blackwidow.getAge();
    blackwidow.showpower();
  
    showHeroPower(blackwidow);

    cout << "------------------------------------------" << endl;

    BrujaEscarlata brujaescarlata;

    brujaescarlata.name = "Wanda Maximoff";
    brujaescarlata.alias = "Bruja Escarlata";
    brujaescarlata.universe = "MCU";

    cout << "Nombre: " << brujaescarlata.name << endl;  
    cout << "Alias: " << brujaescarlata.alias << endl;
    cout << "Universo: " << brujaescarlata.universe << endl;

    brujaescarlata.updateAge(28);  
    brujaescarlata.getAge();
    brujaescarlata.showpower();

   showHeroPower(brujaescarlata);

  cout << "------------------------------------------" << endl;

  Hulk hulk;

  hulk.name = "Bruce Banner";
  hulk.alias = "Hulk";
  hulk.universe = "MCU";

  cout << "Nombre: " << hulk.name << endl;
  cout << "Alias: " << hulk.alias << endl;
  cout << "Universo: " << hulk.universe << endl;

  hulk.updateAge(45);
  hulk.updateAge(-2);
  hulk.getAge();
  hulk.showpower();

  showHeroPower(hulk);
  
  cout << "------------------------------------------" << endl;
  
    return 0;
};