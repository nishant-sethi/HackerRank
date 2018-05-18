#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define SIZE 1000
using namespace std;


int main() {
    long long int a[SIZE]={0};
    long long int sum=0;
    int i,n;
    cin>>n;
    for(i=0;i<n;i++)
        cin>>a[i];
    for(i=0;i<n;i++)
        sum+=a[i];
    cout<<sum; 
    return 0;
}