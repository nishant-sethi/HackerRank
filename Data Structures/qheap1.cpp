#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<climits>
using namespace std;
vector<long> heap;
void upheapify(int i){
    int parent=(i-1)/2;
    while(i>=0 && heap[parent]>heap[i]){
        swap(heap[parent],heap[i]);
        i=parent;
        parent=(i-1)/2;
}
}
void insert(long ele){
    heap.push_back(ele);
    if(heap.size()==1){
    }
    else{
    upheapify(heap.size()-1);
    }
}
void downheapify(int i){
    int l=2*i+1;
    int r=2*i+2;
    int smallest=i;
    if(l<heap.size() && heap[smallest]>heap[l])
        smallest=l;
    if(r<heap.size() && heap[smallest]>heap[r])
        smallest=r;
    if(smallest!=i)
        {
            swap(heap[i],heap[smallest]);
            downheapify(smallest);
        }
}
void del(int ele){
    int idx;
    for(idx=0;idx<heap.size();idx++){
        if(heap[idx]==ele)
            break;
    }
    if(heap.size()==1) heap.pop_back();
    else {heap[idx]=heap[heap.size()-1];
    heap.pop_back();
    downheapify(idx);
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int q,ch;
    long v;
    cin>>q;
    vector<long> ans;
    while(q--){
        cin>>ch;
        switch(ch){
            case 1:cin>>v;
            insert(v);break;
            case 2:cin>>v;
            del(v);break;
            case 3:ans.push_back(heap[0]);
            break;
        }
    }
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}
