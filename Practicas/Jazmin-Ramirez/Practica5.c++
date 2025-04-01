#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;
class Spell
{
private:
string name;
string description;
public:
Spell(const string& name, const string& description): name(name), description(description) {}
void cast() const{cout<<"¡"<<name<<"! "<<description<<endl;}
};

class MagicPerson
{
public:
string name;
int age;
string house;
public:
MagicPerson(const string& name, int age, const string& house): name(name), age(age), house(house) {}
void introduce() const{cout<<""<<name<<" tiene "<<age<<" años y su casa es "<<house<<endl;}
void castSpell(const Spell& spell) const{spell.cast();}
};

class student : public MagicPerson 
{
public:
int yearsAtHogwarts;
string favoirteSpell;
public:
student(const string& name, int age, int yearsAtHogwarts, const string& favoirteSpell, const string& house = "") : MagicPerson(name, age, house), yearsAtHogwarts(yearsAtHogwarts), favoirteSpell(favoirteSpell) {}
void introduce() const{cout<<""<<name<<" tiene "<<age<<" años y lleva "<<yearsAtHogwarts<<" años en hogwarts y su hechizo favorito es "<<favoirteSpell<<endl;}
void castSpell(const Spell& spell) const{spell.cast();}
};

class Professor : public MagicPerson 
{
public:
string subject;
public:
Professor(const string& name, int age, const string& house, const string& subject) : MagicPerson(name, age, house), subject(subject) {}
void introduce() const{cout<<""<<name<<" tiene "<<age<<" años y su casa es "<<house<<" y da clases de "<<subject<<endl;}
void castSpell(const Spell& spell) const{spell.cast();}
};
class SortingHat {
private:
    vector<string> houses = {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"};

public:
 public:
 string sortStudent() {
     static unsigned int counter = 0;
     srand(time(nullptr) * clock() + (++counter));

     int randomIndex = rand() % houses.size();
     randomIndex = (randomIndex + clock() % houses.size()) % houses.size();
   
     return houses[randomIndex];
 }
};

int main()
{
    SortingHat hat;
    student estudiante1("Harry Potter", 11, 1, "Expelliarmus");
    estudiante1.introduce();
    estudiante1.castSpell(Spell("Lumos", "Una luz brillante"));
    cout << "Casa del estudiante: " << hat.sortStudent() << endl;
    cout <<"--------------------------------------------------"<<endl;
  
    student estudiante2("Ron Weasley", 11, 1, "Alohomora");
    estudiante2.introduce();
    estudiante2.castSpell(Spell("Accio", "Atrae objetos"));
    cout << "Casa del estudiante: " << hat.sortStudent() << endl;
    cout <<"--------------------------------------------------"<<endl;

    student estudiante3("Draco Malfoy", 11, 1, "Petrificus Totalus"); 
    estudiante3.introduce();
    estudiante3.castSpell(Spell("Expecto Patronum", "Patronus"));
    cout << "Casa del estudiante: " << hat.sortStudent() << endl; 
    cout <<"--------------------------------------------------"<<endl;

    Professor professor1("Severus Snape", 40, "Slytherin", "Pociones");
    professor1.introduce();
    professor1.castSpell(Spell("Crucio", "Provoca un dolor insopotable"));
    cout <<"--------------------------------------------------"<<endl;

    Professor professor2("Rubeus Hagrid", 40, "Gryffindor", "Cuidado de criaturas mágicas");
    professor2.introduce();
    professor2.castSpell(Spell("Protego", "proteje a los magos"));
    cout <<"--------------------------------------------------"<<endl;

    Professor professore3("Remus Lupin", 40, "Ravenclaw", "Defensa contra las artes oscuras");
    professore3.introduce();
    professore3.castSpell(Spell("Aguamenti", "Aumenta la inteligencia" ));
    cout <<"--------------------------------------------------"<<endl;

    return 0;
};