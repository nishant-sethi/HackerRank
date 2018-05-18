#include<iostream>
#include<string.h>
#include<stdlib.h>
#define max 10000
using namespace std;
int main(){
    char a[max];int c[26],d[26];
    int t;
    cin>>t;
    for(int j=0;j<t;j++){
        int sum=0;int i;
        for(i=0;i<26;i++)
            c[i]=d[i]=0;
        cin>>a;
        if(strlen(a)%2!=0)
            cout<<"-1";
        else{
         for(i=0;i<strlen(a)/2;i++)
                c[a[i]-97]++;
         for(i=strlen(a)/2;i<strlen(a);i++)
                d[a[i]-97]++;
         for(i=0;i<26;i++)
            sum+=abs(c[i]-d[i]);
         cout<<sum/2;
        }
        cout<<"\n";
    }
    return 0;
}
