#include<iostream>
using namespace std;
int main(){
    int loan;
    int rate;
    int months;

    cout<<"Enter loan amount: ";
    cin>>loan;

    cout<<"Enter rate: ";
    cin>>rate;

    cout<<"Enter numbers of months: ";
    cin>>months;


    ///monthly interest = loan amount / rate;
    cout<<"\nMonthly Interest: "<< loan / rate ;
    cout<<"\nYour Interest is "<< (loan/rate) * months;

    return 0;
}
