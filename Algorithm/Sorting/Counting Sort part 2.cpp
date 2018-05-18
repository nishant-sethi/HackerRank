#include <cmath>  
 #include <cstdio>  
 #include <vector>  
 #include <iostream>  
 #include <algorithm>  
 using namespace std;  
 int main() {  
   /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   long long arr[1000000] ={0},i,j,k,x,n;  
   cin>>n;  
   for(i=0;i<n;i++){  
     cin>>x;  
     arr[x]++;  
   }  
   i=0;  
   while(n>0){  
     while(arr[i]>0){  
       cout<<i<<" ";  
       n--;  
       arr[i]--;  
     }  
     i++;  
   }  
   cout<<endl;  
   return 0;  
 } 