#include<iostream>
using namespace std;
int main(){

    int num1,num2,num3;

    cout<<"Enter number 1st number: ";
    cin>>num1;

    cout<<"Enter number 2nd number: ";
    cin>>num2;

    cout<<"Enter number 3rd number: ";
    cin>>num3;

    int max_num = num1;

    if( max_num < num2 ){
        max_num = num2;
    }
    if( max_num < num3 ){
        max_num = num3;
    }
    cout<<"Maximum number: "<<max_num;

    return 0;
}
