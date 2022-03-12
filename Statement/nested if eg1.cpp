#include<iostream>
using namespace std;
int main(){

    int num;
    cout<<"Enter any number: ";
    cin>>num;

    if ( num % 3 == 0 || num % 5 == 0 ){
        if( num % 3 == 0 ){
            cout<<num<<" is dividible with 3\n";
        }else{
            cout<<num<<" is divisible with 5\n";
        }
    }else{
        cout<<num<<" is not divisible with both 3 and 5\n";
    }

    return 0;
}
