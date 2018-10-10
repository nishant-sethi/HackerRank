#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def sumOfSubstrings(num): 
    n = len(num) 
  
    # allocate memory equal  
    # to length of string 
    sumofdigit = [] 
  
    # initialize first value 
    # with first digit 
    sumofdigit.append(int(num[0])) 
    res = sumofdigit[0] 
  
    # loop over all 
    # digits of string 
    for i in range(1, n): 
        numi = int(num[i]) 
  
        # update each sumofdigit 
        # from previous value 
        sumofdigit.append(((i + 1) * 
                        numi + 10 * 
                        sumofdigit[i - 1]) %(10**9+7))
  
        # add current value 
        # to the result 
        res += sumofdigit[i] 
   
    return (res%(10**9+7))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = sumOfSubstrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
