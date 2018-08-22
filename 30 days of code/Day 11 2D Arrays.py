#!/bin/python3

import math
import os
import random
import re
import sys



arr=[]
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
lst=[]
for i in range(4):
    for j in range(4):
        res=sum(arr[i][j:j+3])
        index=(j+(j+3))//2
        res+=arr[i+1][index]
        res+=sum(arr[i+2][j:j+3])
        lst.append(res)

print(max(lst))
