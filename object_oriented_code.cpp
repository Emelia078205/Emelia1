#include <iostream>
using namespace std;


///////////////////// class Company  ////////////////////////

class Company 
{
    string ownerName;
protected:
    string companyName;
public:
    void set(string o, string c) {
        ownerName = o;
        companyName = c;
    }
 
    virtual string getAddress()
    {
        return "Irbid" ;
    }  
  
     virtual void print()
    {
        cout << "Company Name: " << companyName
             << "\nCompany Owner Name: " << ownerName<< endl;
    }

    Company(string o, string c) {
        set(o, c);
    }

    virtual ~Company() {
        cout << " company is closed.\n";
    }
};


///////////////////// class RealCompany  ////////////////////////

class RealCompany : public Company
{
    string address;
    double area;
   
public:
    
    RealCompany(string o, string c, string ad, double a) : Company(o, c) {
         address = ad;
         area = a;
    }
    
    void set(string o, string c, string ad, double a) {
        Company::set(o, c);
        address = ad;
        area = a;
        
    }
    
    string getAddress() {
        return address;
    }
    
    /*  1. Write the print() function to display all information:
      as shown in the sample run. */
  void print(){
      Company::print();
       cout<<"Company Address: "<<address<<endl;
       cout<<"Company Area: "<<area<<endl;
   }
   
    
    ~RealCompany() {
        cout << companyName;
    }
    
};


/////////////////  class OnLineCompany  /////////////////////////////
   
 class OnLineCompany : public Company
 {
    string website;
    
public:
    
    OnLineCompany(string o, string c, string w) : Company(o, c) {
        website = w;
    }
    
    void set(string o, string c, string w) {
        Company::set(o, c);
        website = w;
    }
    
    string getAddress() {
        return website;
    }
    
    
     /*  2) Write the print() function to display all information:
      as shown in the sample run. */ 
   void print(){
        Company::print();
        cout<<"Company Website: "<<website<<endl;
   }
   
   
   
   
    
    ~OnLineCompany() {
        cout << website;
    }
    
};
 
   
// 3)  Write Non-member function ==> showCompanyInfo
void showCompanyInfo(Company * c){
    c->print();
}







//////////////  Complete Main Function    /////////////////////

int main() {
    
   /*  1. Create a dynamic object of Company class points to RealCompany class 
       with the following values: Adam Ali, JUST, Irbid, 500         */
     Company *ptr1=new RealCompany("Adam Ali" , "JUST" , "Irbid" , 500);
     
    

   /*  2. Create a dynamic object of Company class points to OnLineCompany class 
       with the following values: Salma Omar, DressModa, DressModa.com      */
 Company *ptr2=new OnLineCompany("Salma Omar" , "DressModa" , "DressModa.com");
 
   
    
    cout << "**********Real Company Information**********\n";
    // 3. Print the real company information by calling showCompanyInfo function.
    showCompanyInfo(ptr1);
    

    
    cout << "\n**********Online Company Information**********\n";
    // 4. Print the onLine company information by calling showCompanyInfo function.
  showCompanyInfo(ptr2);


    cout << endl;
    
 // 5. Release all dynamically allocated memory used in the program.
 delete ptr1;
 delete ptr2;
 
 

    return 0;
}
