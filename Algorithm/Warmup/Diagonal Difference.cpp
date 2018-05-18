#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define size 100
using namespace std;


int main() {
   int array[size][size]={0};
    int n,i,j,sum=0,a=0,c;
    cin>>n;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            cin>>array[i][j];
        }
    }
    for (i = 0; i < n; ++i)
        {
            sum = sum + array[i][i];
            a = a + array[i][n - i - 1];
        }
    c=abs(sum-a);
    cout<<c;
    return 0;
}