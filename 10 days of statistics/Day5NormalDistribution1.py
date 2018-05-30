'''
Created on May 28, 2018

@author: nishant.sethi
'''
import math

def cmf(case,mean,std):
    z=(case-mean)/(std*(2**0.5))
    error=math.erf(z)
    return (1+error)*0.5

mean=20
std=2
case1=19.5
result1=cmf(case1, mean, std) 
print(round(result1,3))
case2=20
result2=cmf(case2, mean, std)
case3=22
result3=cmf(case3, mean, std)
x=result3-result2
print(round(x,3))
