#include<iostream>
#include<string.h>
#define max 10000
using namespace std;
int main(){
    char a[100000];int odd=0;int flag=0;
    cin>>a;
    int b[26];
    for(int i=0;i<26;i++)
        b[i]=0;
    for(int i=0;i<strlen(a);i++){
        b[a[i]-97]++;
    }
    for(int i=0;i<26;i++){
        if(odd>1){
            flag=1;
            break;
        }
        else if(b[i]%2!=0)
            odd++;
    }
    if(flag==1)
        cout<<"NO";
    else
        cout<<"YES";
    return 0;
}