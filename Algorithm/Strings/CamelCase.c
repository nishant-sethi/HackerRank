#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    char* s = (char *)malloc(10240 * sizeof(char));
    int count=1,i;
    scanf("%s",s);
    for(i=0;i<strlen(s);i++){
        if(s[i]>='A' && s[i]<='Z')
            count++;
    }
    printf("%d",count);
    return 0;
}