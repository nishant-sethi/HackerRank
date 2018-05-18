#include <stdio.h>  
 #include <string.h>  
 #include <math.h>  
 #include <stdlib.h>  
 #include <assert.h>  
 int lonelyinteger(int a_size, int* a) {  
   int flag=1,i,k;  
   for(i=0;i<a_size;i++)  
   {  
     flag=1;  
     for(k=0;k<a_size;k++)  
     {  
       if(i != k && a[i] == a[k])  
        {  
            flag=0;        
        }  
     }  
     if(flag)  
     {  
        return a[i];     
     }  
   }  
   return 0;  
 }  
 int main() {  
   int res;  
   int _a_size, _a_i;  
   scanf("%d", &_a_size);  
   int _a[_a_size];  
   for(_a_i = 0; _a_i < _a_size; _a_i++) {   
     int _a_item;  
     scanf("%d", &_a_item);  
     _a[_a_i] = _a_item;  
   }  
   res = lonelyinteger(_a_size, _a);  
   printf("%d", res);  
   return 0;  
 }  