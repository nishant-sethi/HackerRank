#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    x=5
    y=math.floor(x/2)
    z=y
    for i in range(1,n):
        x=math.floor(x/2)*3
        y=math.floor(x/2)
        z=y+z
    return (z)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
