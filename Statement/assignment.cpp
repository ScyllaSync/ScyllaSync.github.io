#include<iostream>>
using namespace std;
int main(){
    int num;
    string result;

    cout<<"Enter any number: ";
    cin>>num;

    result = (num < 0) ? "The number is negative" : "The number is positive";
    cout<<result;

    return 0;
}
