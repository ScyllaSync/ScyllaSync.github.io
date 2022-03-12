#include<iostream>
using namespace std;
int main(){
    int age;
    cout<<"Enter your age: ";
    cin>>age;

    if( age < 60 ){
        cout<<"You are young.\n";
    }
    else if( age == 60){
        cout<<"You are old.\n";
    }
    else{
        cout<<"You are really old.\n";
    }

    return 0;
}
