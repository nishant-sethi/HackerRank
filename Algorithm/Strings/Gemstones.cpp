#include<iostream>
#include<string.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[26];int count=0;
    for(int i=0;i<26;i++)
        a[i]=0;
    char s[100];
    for(int i=0;i<n;i++){
        cin>>s;
        for(int j=0;j<strlen(s);j++)
            if(a[s[j]-97]<i+1 && a[s[j]-97]==i)
            a[s[j]-97]++;
    }
    for(int i=0;i<26;i++){
        if(a[i]>=n)
            count++;
    }
    cout<<count;
    return 0;
}