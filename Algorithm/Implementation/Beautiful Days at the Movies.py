#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(num):
    rev= 0    
    while(num > 0):    
        Reminder = num %10     
        rev = (rev *10) + Reminder    
        num = num //10 
    return rev
def beautifulDays(i, j, k):
    count=0
    for x in range(i,j+1):
        if abs(x-reverse(x))%k==0:
            count+=1
    return count 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
