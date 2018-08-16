#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    missing=[]
    extra=[]
    for i in t:
        if i not in s:
            missing.append(i)
    for i in s:
        if i not in t:
            extra.append(i)
    count=0
    for i in range(len(s) if len(t)>len(s) else len(t)):
        if s[i]==t[i]:
            count+=1
        else:
            break
    diff1=len(s[count:])
    diff2=len(t[count:])
    if len(s)+len(t)<=k or ((k-(diff1+diff2))%2==0 and diff1+diff2<=k):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()