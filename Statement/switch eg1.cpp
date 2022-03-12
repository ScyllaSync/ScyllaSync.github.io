#include<iostream>
using namespace std;
int main(){
    int dow;
    cout<<"Enter number between 1 to 7: ";
    cin>>dow;

    switch(dow){
    case 1:
        cout<<"\nSunday";
        break;
    case 2:
        cout<<"\nMonday";
        break;
    case 3:
        cout<<"\nTuesday";
        break;
    case 4:
        cout<<"\nWednesday";
        break;
    case 5:
        cout<<"\nThursday";
        break;
    case 6:
        cout<<"\nFriday";
        break;
    case 7:
        cout<<"\nSaturday";
        break;
    default:
        cout<<"\nWrong numbers of days";
    }

    return 0;
}
