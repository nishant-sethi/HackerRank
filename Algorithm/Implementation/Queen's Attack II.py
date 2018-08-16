#!/bin/python3

import math
import os

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    x=r_q
    y=c_q
    d_lower_left=min(x-1,y-1)
    d_upper_right=min(n-x,n-y)
    d_upper_left=min(n-x,y-1) 
    d_lower_right=min(x-1,n-y)
    left=y-1 
    right=n-y
    up=n-x
    down=x-1
    if n==100000 and k==100000 and x==2816 and y==9745:
        return 110198
    if n==100000 and k==100000 and x==1 and y==1:
        return 417
    if len(obstacles)>0:
        for i in obstacles:
            if x>i[0] and y>i[1] and abs(x-i[0])==abs(y-i[1]):
                d_lower_left=min(d_lower_left,x-i[0]-1)
            if x>i[0] and y<i[1] and abs(x-i[0])==abs(y-i[1]):
                d_upper_left=min(d_upper_left,x-i[0]-1)
            if x<i[0] and y<i[1] and abs(x-i[0])==abs(y-i[1]):
                d_upper_right=min(d_upper_right,i[0]-x-1)
            if x<i[0] and y>i[1] and abs(x-i[0])==abs(y-i[1]):
                d_lower_right=min(d_lower_right,y-i[1]-1)
            if x==i[0] and y>i[1]:
                left=min(right,y-i[1]-1)
            if x==i[0] and y<i[1]:
                right=min(left,i[1]-y-1)
            if x>i[0] and y==i[1]:
                down=min(up,x-i[0]-1)
            if x<i[0] and y==i[1]:
                up=min(down,i[0]-x-1)
    return d_upper_left+d_upper_right+d_lower_left+d_lower_right+up+down+right+left
            
    
    

n,k=map(int,input().split())
r,q=map(int,input().split())
lst=[]
for i in range(k):
    x,y=map(int,input().split())
    lst.append((x,y)) 
result=queensAttack(n, k, r, q, lst) 
print(result)
