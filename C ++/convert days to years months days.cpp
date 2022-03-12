#include<iostream>
using namespace std;
int main(){
    int totalDays;

    cout<<"Enter no of days: ";
    cin>>totalDays;

    int years = totalDays/365;
    int months =  (totalDays%365)/30;
    int days = (totalDays%365)%30;

    cout<<"Years: "<<years;
    cout<<"\nMonths: "<<months;
    cout<<"\nDays: "<<days;

    return 0;
}
