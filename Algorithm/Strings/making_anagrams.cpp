#include<iostream>
#include<string.h>
#include<stdlib.h>
#define max 100000
using namespace std;
int main(){
    char a[max],b[max];
    cin>>a>>b;
    int c[26],d[26],sum=0;
    for(int i=0;i<26;i++)
        c[i]=d[i]=0;
    for(int i=0;i<strlen(a);i++){
         c[a[i]-97]++;
    }
    for(int i=0;i<strlen(b);i++){
         d[b[i]-97]++;
    }
    for(int i=0;i<26;i++){
            sum+=abs(c[i]-d[i]);
    }
    cout<<sum;
    return 0;
}
