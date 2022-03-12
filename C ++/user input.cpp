#include<iostream>
using namespace std;
int main(){
    int empID;
    int salary;
    string name;
    string address;
    float bonus;

    ///user input
    cout<<"Enter Employee ID : ";
    cin>>empID;
    cin.ignore();
    cout<<"Enter name: ";
    ///cin>>name;
    getline(cin,name);
    cout<<"Enter address: ";
    ///cin>>>address;
    getline(cin,address);
    cout<<"Enter salary : ";
    cin>>salary;
    cout<<"Enter bonus: ";
    cin>>bonus;

    cout<<"\n       Employee Information          ";
    cout<<"\nID: "<<empID;
    cout<<"\nSalary: "<<salary;
    cout<<"\nName : "<<name;
    cout<<"\nAddress: "<<address;
    cout<<"\nBonus: "<<bonus;


    cout<<"ID = "<<empID;

    return 0;
}
