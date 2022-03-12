#include<iostream>
using namespace std;
int main(){
    char grade;
    cout<<"Enter your grade: ";
    cin>>grade;

    bool result = true;

    switch(grade){
    case 'A':
        cout<<"Excellent";
        break;
    case 'B':
        cout<<"Credit";
        break;
    case 'C':
        cout<<"Well done";
        break;
    case 'D':
        cout<<"Pass";
        break;
    case 'E':
        cout<<"Fail";
        break;
    default:
        cout<<"Invaid grade";
        result = false;
    }

    if ( result == 1){
        cout<<"\nYour grade is "<<grade;
    }

    return 0;
}
