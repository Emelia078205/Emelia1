#include <iostream>
using namespace std;

//  Write class Box here:
class Box{
private:
   double length;
   double width;
   double height;
public:
   void setAllInfo(double l, double w, double h)
      {
        if(l>0 && w>0 && h>0) {
        length=l;
        width=w;
        height=h;
        }
         else{
         cout<<"error:invalid values"<<endl;
        }
      }
     ///////////////////////////
     void setHeight(double h){
         if(h>0)
         height=h;
         else
         cout<<"not valid value"<<endl;
     }
    ///////////////////////
     void getHeight( double &h) const
    {
        h=height;
    }
    /////////////////
     double getWidth()const
     {
         return width;
     }
    ////////////////
    double  getVolume()const
    {
        return length * width * height ;
    }
   ///////////////// 
   void getAllInfo(double &l,double &w,double &h);
   void print()const;
   bool compare(const Box & b)const;
};//end of class
void Box::getAllInfo(double &l,double &w,double &h)
{
    l=length;
    w= width;
    h=height;
}
/////////
void Box::print()const
{
    cout<<"length = "<<length<<", width = "<<width<<", height = "<<height<<endl;
}
/////////
bool Box::compare(const Box & b)const 
{
    return (length == b.length && width == b.width && b.height == height);
}

int main() 
{
    
//Step 1: Declare 2 objects of type Box (box1 and box2). 
Box box1;
Box box2;


// Step 2: Prompt the user to input 3 values to set the value of box1
double length , width , height;
cout << "Enter length, width, and height for box1:"<<endl;
cin >> length >> width >> height;
  box1.setAllInfo(length , width , height ); 
   
   

// Step 3: Set values for box2
box2.setAllInfo(2,7,4);


// Step 4: Print box1 and box2 values
cout << "Box 1: ";
box1.print();

cout << "Box 2: ";
box2.print();


// Step 5: Print the volume of box1
cout << "Volume of Box 1: " ;
  cout<<box1.getVolume(); 
    

// Step 6: Increment the height of box1 by 3
box1.setHeight(height+3);


// Step 7: Print box1 and box2 values again
cout << "
Box 1 after height increment: ";
 box1.print();
 
 
cout << "Box 2 remains the same: ";
box2.print();



// Step 8: Compare box1 and box2
    if(box1.compare(box2))
    cout<<"The boxes are equal.";
    else
    cout<<"The boxes are not equal.";
    
    
    
return 0;
}
