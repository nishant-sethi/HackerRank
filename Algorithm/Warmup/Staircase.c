#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int row, c, n, temp;
 

   scanf("%d",&n);
 
   temp = n;
 
   for ( row = 1 ; row <= n ; row++ )
   {
      for ( c = 1 ; c < temp ; c++ )
         printf(" ");
 
      temp--;
 
      for ( c = 1 ; c <=row ; c++ )
         printf("#");
 
      printf("\n");
   }
  
    return 0;
}