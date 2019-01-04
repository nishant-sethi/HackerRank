#include<stdio.h>
int main(){
    long long int n,base=1,bin=0,r,max=0,count=0;
    scanf("%d",&n);

    while(n>0){
        r=n%2;
        n=n/2;
        if(r==1){
            count++;
        }
        else{
            if(count>=max){
                max=count;
            }
            count=0;
        }
        
    }
    printf("%d",max);
    return 0;
}
