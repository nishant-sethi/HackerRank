'''
Created on May 22, 2018

@author: nishant.sethi
'''
import numpy as np
n=int(input())
num=[int(x) for x in input().split()]
num.sort()
s1=[]
s2=[]
mid=n//2
if n%2!=0:
    s1=num[0:mid]
    s2=num[mid+1:]
else:
    s1=num[0:mid]
    s2=num[mid:]
if len(s1)%2==0:
    mid=(len(s1)//2)-1
    result=s1[mid]+s1[mid+1]
    print(result//2)
else:
    print(s1[len(s1)//2])
if len(num)%2==0:
    mid=(len(num)//2)-1
    result=num[mid]+num[mid+1]
    print(result//2)
else:
    print(num[n//2])
if len(s2)%2==0:
    mid=(len(s2)//2)-1
    result=s2[mid]+s2[mid+1]
    print(result//2)
else:
    print(s2[len(s1)//2])  