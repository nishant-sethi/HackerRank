#include<iostream>
#define max 10000
using namespace std;
int main(){
    int a[max];int temp;
    for(int i=0;i<max;i++)
        a[i]=0;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=1;i<n;i++){
        for(int j=0;j<i;j++){
            if(a[i]<a[j]){
                temp=a[j];
                a[j]=a[i];
                a[i]=temp;
        }
        }
         for(int k=0;k<n;k++)
            cout<<a[k]<<" ";
        cout<<"\n";
    }
    return 0;
}
