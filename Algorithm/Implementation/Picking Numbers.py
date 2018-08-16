#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    dct=dict(Counter(a))  
    max_integers=0
    lst_keys=list(dct.keys())
    lst=sorted(lst_keys)
    if len(lst)==1:
        max_integers=dct[lst[0]]
    else:
        for i in range(0,len(lst)-1):
            if abs(lst[i+1]-lst[i])<=1:
                curr=dct[lst[i]]+dct[lst[i+1]]
            else:
                curr=max(dct[lst[i]],dct[lst[i+1]])
            if max_integers<curr:
                    max_integers=curr
    return max_integers

n=int(input())
a=[int(x) for x in input().split()]
print(pickingNumbers(a))
