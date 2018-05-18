#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int v,n;
    cin>>v>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<n;i++){
        if(a[i]==v){
            cout<<i;
            break;
        }
    }
    return 0;
}