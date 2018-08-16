#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    l=[]
    for i in range(0,len(a)-1):
        for j in range(1,len(a)):
            if a[i]==a[j] and i!=j:
                x=abs(j-i)
                l.append(x)
    if len(l)==0:
        return -1
    else:
        return min(l) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
