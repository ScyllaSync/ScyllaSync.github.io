#include<iostream>
using namespace std;
///global space(global variable)
int a = 10;

void display(){
     ///inside function
     int a = 20;
     cout<<"\n value of a inside fun: "<<a;
}
void displayAnother(int a){///parameter
     cout<<"\n Value of a inside fun parameter: "<<a;
}
 int main(){
     cout<<"Value of a: "<<a;
     display();///function calling statement;
     displayAnother(30);
     return 0;
}
