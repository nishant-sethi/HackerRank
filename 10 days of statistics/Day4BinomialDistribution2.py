'''
Created on May 25, 2018

@author: nishant.sethi
'''
import math
def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 0.12, 10
for i in range(0,3):
    b += bi_dist(i, n, p)   
print("%.3f" %b)
b=0
for i in range(2,11):
    b += bi_dist(i, n, p)   
print("%.3f" %b)