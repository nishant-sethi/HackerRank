#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define SIZE 1000
using namespace std;


int main() {
    int a[SIZE]={0};
    int sum=0,i,n;
    cin>>n;
    for(i=0;i<n;i++)
        cin>>a[i];
    for(i=0;i<n;i++)
        sum+=a[i];
    cout<<sum;
    return 0;   
}