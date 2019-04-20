#!/bin/python3

import math
import os
import random
import re
import sys


def d_rotations(a,n,d):
    b=[0]*n
    for i in range(n):
        b[(i+n-d)%n]=a[i]
    return b

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    a=d_rotations(a,n,d)
    for i in range(n):
        print(a[i],end=" ")
