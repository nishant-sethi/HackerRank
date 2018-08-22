#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int t;
    char s[100000],a[5000],b[5000];
    int i,j,k,x;
    scanf("%d",&t);
    for(x=0;x<t;x++){
    scanf("%s",s);
    j=0;k=0;
    for(i=0;i<5000;i++)
        a[i]=b[i]='\0';
    for(i=0;i<strlen(s);i++){
        if(i%2==0){
            a[j]=s[i];
            j++;
        }
        else{
            b[k]=s[i];
            k++;
        }
    }
        printf("%s %s\n",a,b);
    }
    
    return 0;
}
