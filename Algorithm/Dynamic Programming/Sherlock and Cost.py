#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(a):
    ix = [0]
    ex = [0]
    
    for i in range(1,n):
        ex.append(ix[i-1]+a[i-1]-1)
        tmp = ex[i-1]
        if i > 1:
            tmp = max(tmp,ex[i-2])
        ix.append(a[i]-1+tmp)
    
    return max(ex[n-1],ix[n-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
