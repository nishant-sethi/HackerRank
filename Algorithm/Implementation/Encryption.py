#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l=len(s)
    x=math.floor(l**0.5)
    y=math.ceil(l**0.5)
    j=0
    i=0
    a=''
    z=0
    while j!=y:
        i=z
        while i<=l-1:
            a+=s[i]
            i+=y
        a+=' '
        j+=1
        z+=1
    print(a)
    
s = input()
encryption(s)

