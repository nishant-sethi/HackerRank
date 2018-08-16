#!/bin/python

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    important=[]
    unimportant = []
    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            unimportant.append(luck)
    important.sort()
    important = important[::-1]
    for u in range(k,len(important)):
        important[u] *=-1
    return sum(important)+sum(unimportant)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
