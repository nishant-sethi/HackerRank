#include<iostream>
#include<string.h>
#define max 100000
using namespace std;
int main(){
    char str[max];int t;
    cin>>t;
    for(int j=0;j<t;j++){
        int _count=0;
        cin>>str;
        int n=strlen(str);
        for(int i=0;i<n-1;i++){
            if(str[i+1]==str[i])
                _count++;
        }
        cout<<_count;
        cout<<"\n";
    }
    return 0;
}