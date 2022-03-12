#include<iostream>
using namespace std;
int main(){
    int price;
    int discount;

    cout<<"Enter Product Price: ";
    cin>>price;

    cout<<"Discount Value: ";
    cin>>discount;

    cout<<"After discount,prize : "<<price-(price*discount/100);

    return 0;
}
