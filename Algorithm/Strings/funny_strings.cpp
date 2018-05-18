#include<iostream>
#include<string.h>
#include<stdlib.h>
#define max 100000
using namespace std;
int main(){
    char str[max];int t;
    cin>>t;
    for(int j=0;j<t;j++){
        int flag=0;
        //cout<<"Enter the string :\n";
        cin>>str;
        char rev[max];
        int n=strlen(str);
        for(int i=0;i<strlen(str);i++)
            rev[i]=str[n-i-1];
        for(int i=1;i<strlen(str);i++){
            //cout<<str<<"\n"<<rev<<str[i]-str[i-1]<<"\n"<<(rev[i]-rev[i-1])<<"\n";
            if(abs(str[i]-str[i-1])!=abs(rev[i]-rev[i-1])){
                flag=1;
                break;
            }
        }
        if(flag==0)
            cout<<"Funny";
        else
            cout<<"Not Funny";
        cout<<"\n";
    }
    return 0;
}
