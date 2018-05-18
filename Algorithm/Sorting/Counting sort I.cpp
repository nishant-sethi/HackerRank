#include <cmath>  
 #include <cstdio>  
 #include <vector>  
 #include <iostream>  
 #include <algorithm>  
 using namespace std;  
 int main() {  
   /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
   long long arr[1000000]={0},n,i,j,k,x;  
   cin>>n;  
   for(i=0;i<n;i++){  
     cin>>x;  
     arr[x]++;  
   }  
   for(i=0;i<100;i++)  
     {  
     cout<<arr[i]<<" ";  
   }  
   cout<<endl;  
   return 0;  
 }  