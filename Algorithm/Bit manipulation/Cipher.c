#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
       int i,n,k,f,j,x;
       scanf("%d%d",&n,&k);
       char s[n+k-1],a[n];
       scanf("%s",s);
       a[0] = s[0] - '0';
       f = 0;
       for(i=1;i<n;i++)
       {
              f = f^a[i-1];
              if(i>=k)
              {
                     f = f^a[i-k];
              }
              a[i] = (int)(s[i]- '0')^f;
       }
       for(i=0;i<n;i++)
       {
              printf("%d",a[i]);
       }
       printf("\n");
    return 0;
}