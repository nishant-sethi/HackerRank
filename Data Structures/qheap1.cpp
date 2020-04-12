#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
vector <int> a;
void downheapify( int i, int n){
    int min=i;
    int l=2*i+1;
    int r=2*i+2;
    if(l<n && a[l]<a[i]){
        min=l;
    }
    if(r<n && a[r]<a[min]){
        min=r;
    }
    if(min!=i){
        int temp=a[i];
        a[i]=a[min];
        a[min]=temp;
        downheapify(min,n);
    }
}
void upHeapify(int n, int x){
    int i=n-1;
    int p=(i-1)/2;
    while(p>=0 && a[p]>a[i]){
        swap(a[i],a[p]);
        i=p;
        p=(i-1)/2;
    }   
}
void insert(int x){
    a.push_back(x);
    int n=a.size();
    if(n!=1)
    upHeapify(n,x);
}

void deleting( int e){
    
    int pos;
    for(int i=0; i<a.size(); i++){
        if(a[i]==e){
            pos=i;
            break;
        }
    }
    int temp=a[pos];
    a[pos]=a[a.size()-1];
    a[a.size()-1]=temp;
    a.pop_back();
    int n=a.size();
    downheapify(pos,n);
}

int main() {
    int q,type;
    cin>>q; 
    int ans[q];
    int t=0;
    for(int i=1;i<=q; i++){
        cin>>type;
        switch(type){
            case 1:
                int x;
                cin>>x;
                insert(x);
                break;
            case 2:
                int e;
                cin>>e;
                deleting(e);
                break;
            case 3:
                ans[t++]=a[0];
                break;    
        }
    }
    for(int i=0; i<t; i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}
