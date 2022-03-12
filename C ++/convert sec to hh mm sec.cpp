#include<iostream>
using namespace std;
int main(){
    int totalSec;

    cout<<"Enter total seconds: ";
    cin>>totalSec;

    int hr = totalSec/3600;
    int mins = (totalSec%3600)/60;
    int sec = (totalSec%3600)%60;

    cout<<"Hours: "<<hr;
    cout<<"\nMinutes: "<<mins;
    cout<<"\nSeconds: "<<sec;

    return 0;
}

