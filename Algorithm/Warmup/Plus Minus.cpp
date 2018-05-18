#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
#define size 100
using namespace std;


int main() {
     int a[size]={0};
     float n;
     float count_zero,count_pos,count_neg;
    cin>>n;
    int i;
    for(i=0;i<n;i++)
        cin>>a[i];
    int neg=0;
    float pos=0;int zero=0;
    for(i=0;i<n;i++){
        if(a[i]<0)
            neg++;
        else if(a[i]==0)
            zero++;
        else
            pos++;
    }
    count_zero=float(zero/n);
    count_pos=float(pos/n);
    count_neg=float(neg/n);
    cout<<setprecision(3)<<count_pos<<endl;
    cout<<setprecision(3)<<count_neg<<endl;
    cout<<setprecision(3)<<count_zero;
    return 0;
}