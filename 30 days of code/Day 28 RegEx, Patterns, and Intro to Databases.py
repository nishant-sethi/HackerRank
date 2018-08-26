#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lst=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.match(r'[a-z]+',firstName) and len(firstName)<=20:
            if re.match(r'[a-z@.]+',emailID) and len(emailID)<=40 and emailID.endswith('@gmail.com'):
                lst.append(firstName)
                
    for i in sorted(lst):
        print(i)
