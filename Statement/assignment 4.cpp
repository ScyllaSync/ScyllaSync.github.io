#include<iostream>
using namespace std;
int main(){
    int programming;
    int english;
    int math;

    cout<<"Enter your Programming marks: ";
    cin>>programming;

    cout<<"Enter your English marks: ";
    cin>>english;

    cout<<"Enter your Math marks: ";
    cin>>math;

    int max_marks = programming;

    if( max_marks < english){
        max_marks = english;
    }

    if( max_marks < math){
        max_marks = math;
    }

    cout<<"Subject that got highest mark is"<<max_marks;

    return 0;
}
