#include<iostream>
using namespace std;
int main(){
    int a = 20, b = 10, c = 15, d = 5;
    int e;

    e = ( a+b ) * c / d;
    cout<<"( a+b ) * c / d is "<<e;

    e = (( a + b ) * c ) / d;
    cout<<"\n(( a + b ) * c ) / d is "<<e;

    e = ( a + b ) * ( c / d );
    cout<<"\n( a + b ) * ( c / d ) is "<<e;

    e = a + ( b * c ) / d;
    cout<<"\na+ ( b * c ) / d is "<<e;
    return 0;
}
