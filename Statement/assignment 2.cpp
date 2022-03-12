#include<iostream>
using namespace std;
int main(){

    int price;
    int quantity;



    cout<<"Enter Quantity: ";
    cin>>quantity;

    cout<<"Enter price: ";
    cin>>price;

    if( quantity * price < 5000){
        cout<<"Total expense: "<<quantity * price;
    }
    else if( quantity * price > 5000){
        cout<<"Total expense: "<<(quantity*price)-(quantity * price* 0.1);
    }

    return 0;
}
