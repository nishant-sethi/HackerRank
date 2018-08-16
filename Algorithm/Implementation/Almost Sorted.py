#!/bin/python3

import math
import os
import random
import re
import sys


def arraySortedOrNot(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

def almostSorted(arr):
    if arraySortedOrNot(arr):
        print("yes")
    else:
        copy_arr=sorted(arr)
        beg=0
        end=0
        #print(arr,copy_arr)
        for i in range(len(arr)):
            if arr[i]!=copy_arr[i]:
                beg=i
                break
        for i in range(len(arr)-1,0,-1):
            if arr[i]!=copy_arr[i]:
                end=i
                break
                
        temp_swap=arr.copy()
        temp_swap[beg],temp_swap[end]=temp_swap[end],temp_swap[beg]
        
        temp_reverse=arr.copy()
        #print(arr,temp_swap,temp_reverse)
        #print(beg,end)
        a=temp_reverse[0:beg]
        b=temp_reverse[beg:end+1]
        #print(b)
        z=b[::-1]
        #print(b[::-1])
        c=temp_reverse[end+1:]
        temp_reverse=a+z+c
        #print(a,z,c,temp_reverse)
        
        if arraySortedOrNot(temp_swap) and arraySortedOrNot(temp_reverse):
            print('yes')
            print('swap',beg+1,end+1)
        else:
            if arraySortedOrNot(temp_swap):
                print('yes')
                print('swap',beg+1,end+1)
            elif arraySortedOrNot(temp_reverse):
                print('yes')
                print('reverse',beg+1,end+1)
            else:
                print('no')
                
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
