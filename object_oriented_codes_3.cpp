#include <iostream>
using namespace std;

class Box {
private:
    double length;
    double width;
    double height;

public:
    // Default constructor
    Box(){
        length=0;
        width=0;
        height=0;
    }
    // Parameterized constructor prototype 
    Box (double l, double w ,double h);

    // Destructor Prototype
    ~Box();

    // Set height
    void setHeight(double h) {
        if (h > 0) {
            height = h;
        } else {
            cout << "Height must be greater than 0." << endl;
        }
    }

    // Set all dimensions
    void setAllInfo(double l, double w, double h) {
        if (l > 0 && w > 0 && h > 0) {
            length = l;
            width = w;
            height = h;
        } else {
            cout << "Invalid dimensions. All dimensions must be greater than 0." << endl;
            length=width=height=0;
        }
    }

    // Get height
    void getHeight(double& h) const {
        h = height;
    }

    // Get width
    double getWidth() const {
        return width;
    }

    // Get volume
    double getVolume() const {
        return length * width * height;
    }

    // Get all dimensions
    void getAllInfo(double& l, double& w, double& h) const {
        l = length;
        w = width;
        h = height;
    }

    // Print dimensions
    void print() const {
        cout << "Length: " << length << " , Width: " << width << " , Height: " << height << endl;
    }
};

// Parameterized constructor implementation  
Box:: Box (double l, double w ,double h){
    /*  if (l > 0 && w > 0 && h > 0) {
            length = l;
            width = w;
            height = h;
        } else {
            cout << "Invalid dimensions. All dimensions must be greater than 0." << endl;
            length=width=height=0;
        }*/
   setAllInfo(l,w,h) ;
    
}


// Destructor implementation 
  Box::~Box(){
      cout<<"Goodbye, Box! ";
      //  cout << "Length: " << length << " , Width: " << width << " , Height: " << height << endl;
      print();
  }


int main() {
    // Create box1 using default constructor
    Box box1 ;

    // Create box2 using parameterized constructor
    Box box2(8, 10, 3);

    // Print initial values
    cout << "Box1 values: ";
      box1.print();
    cout << "Box2 values: ";
       box2.print();

    // Print the volume of box2
    cout << "Volume of Box2: " <<   box2.getVolume()   << endl;
    
    // Prompt user for new dimensions for box1
    double newLength, newWidth, newHeight;
    cout << "Enter the length, width, and height for Box1:"<<endl;
    cin >> newLength >> newWidth >> newHeight;
    box1.setAllInfo(newLength,newWidth,newHeight);

    // Set new dimensions for box2
    box2.setAllInfo(2, 7, 4);
    // Print updated values
    cout << "Updated Box1 values: ";
     box1.print();
    cout << "Updated Box2 values: ";
     box2.print();

    // Print the updated volume of box1
    cout << "Updated volume of Box1: " <<box1.getVolume() << endl;

    return 0;
}
