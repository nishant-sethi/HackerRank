'''
Created on May 21, 2018

@author: nishant.sethi
'''
import math
a=int(input())
b=int(input())
c=(a**2+b**2)**0.5
result=round(math.degrees(math.asin(a/c)))
print(str(int(result))+'°')