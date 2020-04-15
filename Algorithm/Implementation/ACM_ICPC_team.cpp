#include <bits/stdc++.h>

using namespace std;

vector <string> v;
int main(){
    int n,m;
    string s;
    cin >> n >> m;
    for(int i=0; i<n; i++){
        cin>>s;
        v.push_back(s);
    }
    int max=0;
    int count=0;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
           int val = 0;
            for(int k=0; k<m; k++){
                if(v[i][k]=='1' || v[j][k]=='1'){
                    val++;
                }
                if(max<val){max = val;
                count = 1;
                }
                else if(max==val){count++;
                }
            }
        }
    }
    cout<<max<<endl<<count;
}

    

    
