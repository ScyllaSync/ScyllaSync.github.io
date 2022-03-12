#include<iostream>
using namespace std;
int main(){
    int time;
    cout<<"Enter time:";
    cin>>time;

    string result = ( time < 10 ) ? "Good morning" : (time < 20 ? "Good Day" : "Good Evening");
    cout<<result;

    return 0;
}
