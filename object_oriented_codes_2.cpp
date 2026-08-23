#include <iostream>
#include<string>
using namespace std;

class Vehicle {
private:
    int wheels;
    double price;
    string color;
public:
    Vehicle() {
        wheels = 4;
        price = 10000;
        color = "White";
    }
    Vehicle(int w, double p, string c) {
        wheels = w;
        price = p;
        color = c;
    }
    void initialize(int w, double p, string c) {
        wheels = w;
        price = p;
        color = c;
    }
    void print() {
        cout << "Wheels: " << wheels << "\nPrice: "
             << price << "\nColor: " << color << endl;
    }
    double getPrice() {
        return price;
    }
    ~Vehicle() {
        cout << "Goodbye Vehicle -> Wheels: "
             << wheels << ", Price: " << price
             << ", Color: " << color << endl;
    }
};

class Car: public Vehicle
{
private:
    int load;
    double weight;
    string optionsList[50];
    int options;
public:
    // Default Constructor
    Car(){
        load=5;
        weight=2000;
        options=0;
    }
    // Parameterized Constructor
    Car(int w , double p , string c , int lod , double weigh):Vehicle(w, p, c){
        load=lod;
        weight=weigh;
    }
    // SetCar function
    void SetCar(int wh , double pr , string col , int lod , double weigh){
        initialize(wh , pr , col);
        load=lod;
        weight=weigh;
    }
    // Print function
    void print()
    {
        Vehicle::print();
        cout<<"Load (Passengers): " << load<<endl;
        cout<<"Weight: " << weight << endl;
        cout << "Options List (" << options << "):"<<endl;
        for(int i=0;i<options;i++)
            cout<<optionsList[i]<<endl;
    }
    // Add option
    void addOption(string opt) {
        if(options<50)
            optionsList[options++]=opt;
        else
            cout<<"Option list is full"<<endl;
    }
    //Destructor
    ~Car() {
        cout << "Goodbye Car -> Load: " << load << ", Weight: " << weight << endl;
    }
};

int main()
{
    // 1. Declare an object of type Car called c1.
    Car c1;
    // 2. Set all the data members of object c1
    c1.SetCar(4 , 18000 , "Black" , 4 , 125);
    // 3. Add two options: "GPS" and "senseors"
    c1.addOption("GPS");
    c1.addOption("Sensors");
    // 4. Print all information for the object c1
    cout << "\n--- Car c1 Info ---\n" << endl;
    c1.print();
    // 5. Print the price of the car c1
    cout << endl << "Price of c1: " << c1.getPrice() << endl;
    // 6. Declare a dynamic object of type Car
    Car *pCar = new Car(6,25000,"Red",12,5000);
    // 7. Add One option GPS
    pCar->addOption("GPS");
    // 8. Print all information for the dynamic object
    cout << "\n--- Dynamic car Info ---\n" << endl;
    pCar->print();
    cout<<endl;
    // 9. Stop the services of pCar car
    delete pCar;

    // 10. Prompt the user to enter values and declare c2
    int wheels;
    double price;
    string color;
    int load;
    double weight;
    cout << "\nEnter car details:\n";
    cout << "Wheels: ";
    cin >> wheels;
    cout << "Price: ";
    cin >> price;
    cout << "Color: ";
    cin >> color;
    cout << "Load (Passengers): ";
    cin >> load;
    cout << "Weight: ";
    cin >> weight;
    Car c2;
    c2.SetCar(wheels , price , color , load , weight);
    // 11. Print vehicle information from c2
    cout << "\n--- Car c2 Info ---\n" << endl;
    c2.print();
    return 0;
}
