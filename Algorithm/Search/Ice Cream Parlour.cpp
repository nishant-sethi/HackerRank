#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t,c,l;
    cin>>t;
    while(t--)
    {
        cin>>c>>l;
    int a[l];
    for(int i=0;i<l;i++)
        cin>>a[i];
    for(int j=0;j<l-1;j++)
    {
        int k=c-a[j];
        for(int i=j+1;i<l;i++)
        {
            if(a[i]==k)
            {
                cout<<j+1<<" "<<i+1<<endl;
            }
        }
    }
    }
    return 0;
}