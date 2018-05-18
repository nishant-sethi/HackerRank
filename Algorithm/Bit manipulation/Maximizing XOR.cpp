#include<iostream>
#include<stdlib.h>
using namespace std;
int main(){
   int t;
   int max;
   int l,r;
    cin>>l>>r;
    max=-1;
    for(int j=l;j<=r;j++){
        for(int k=l;k<=r;k++){
            if(max<(j^k))
                max=j^k;
        }
    }
    cout<<max<<"\n";
   return 0;
}