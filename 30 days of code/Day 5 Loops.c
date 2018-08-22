#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int N,i; 
    scanf("%d",&N);
    for(i=1;i<=10;i++)
        printf("%d x %d = %d\n",N,i,N*i);
    return 0;
}
