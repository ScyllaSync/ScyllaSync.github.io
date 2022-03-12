#include<iostream>
using namespace std;
int main(){
    string uName;
    string uPass;

    cout<<"Enter username: ";
    cin>>uName;

    cout<<"Enter password: ";
    cin>>uPass;

    if( uName == "mmit" && uPass == "admin123" ){
        cout<<"Login success";
    }
    else if( uName != "mmit" && uPass != "admin123"){
        cout<<"Both username and password are incorrect";
    }
    else if( uName == "mmit" ){
        cout<<"Only username match";
    }
    else if( uPass == "admin123" ){
        cout<<"Only password match";
    }



    return 0;
}
