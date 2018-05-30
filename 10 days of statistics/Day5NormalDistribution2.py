'''
Created on May 28, 2018

@author: nishant.sethi
'''
import math

def cmf(case,mean,std):
    z=(case-mean)/(std*(2**0.5))
    error=math.erf(z)
    return (1+error)*0.5

mean=70
std=10

case1=80
result1=1-cmf(case1, mean, std) 
print(round(result1*100,2)) 

case1=60
result1=1-cmf(case1, mean, std)
print(round(result1*100,2)) 

case3=60
result3=cmf(case3, mean, std)
print(round(result3*100,2)) 


