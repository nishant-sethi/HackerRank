#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int x1; 
    int v1; 
    int x2; 
    int v2; 
    int flag=0;
    scanf("%d %d %d %d",&x1,&v1,&x2,&v2);
    if(x2>x1 && v2>v1)
        printf("NO");
    else if(x1>x2 && v1>v2)
        printf("NO");
    else if(x1>x2 && v1==v2)
        printf("NO");
    else if(x2>x1 && v1==v2)
        printf("NO");
    else if(x1>x2 && v1<v2){
        if(x1-x2%v2-v1==0)
            printf("YES");
        else
            printf("NO");
    }
    else if(x1<x2 && v1>v2){
        if((x2-x1)% (v1-v2)==0)
            printf("YES");
        else
            printf("NO");
    }
    return 0; 
}