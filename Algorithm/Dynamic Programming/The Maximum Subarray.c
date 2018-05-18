#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<ctype.h>
int allnegative(long long int a[],long int n){
    int i;
    for(i=0;i<n;i++){
        if(a[i]>0){
            return 0;
        }
    }
    return 1;
}
long long int maximum(long long int a,long long int b){
    return (a>b)? a:b;
}
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    long long int n;
    long long int i,j,sum,max_c,max_nc;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%lld",&n);
        long long int a[n];
        for(j=0;j<n;j++)
            scanf("%lld",&a[j]);
        max_c=a[0],sum=0,max_nc=0;
        for(j=0;j<n;j++){
            sum=sum+a[j];
            if(sum<0)
                sum=0;
            else if(max_c<sum)
                max_c=sum;
        }
        if(allnegative(a,n)){
            max_nc=a[0];
            for(j=1;j<n;j++)
                max_nc=maximum(max_nc,a[j]);
            max_c=max_nc;
        }
        else{
            for(j=0;j<n;j++){
                if(a[j]>=0)
                    max_nc+=a[j];
            }
        }
        printf("%lld %lld\n",max_c,max_nc);
    }
    return 0;
}