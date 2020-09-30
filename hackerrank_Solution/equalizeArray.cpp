#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
    //after sorting, check for adjacent elements 
    sort(a,a+n);
    //consider first element as max ,iterate from
    //2 element to the end , if found max equal to arr[i]
    //increase c and update maxi with c

    int max=a[0];
    int c=1,maxi=1;
    for(int i=1;i<n;i++){
        if(a[i]==max){
            c++;
            if(c>maxi){
                maxi=c;
            }
        }
        else{
            max=a[i];
            c=1;
        }        
    }
    cout<<n-maxi<<endl;
    return 0;
}



