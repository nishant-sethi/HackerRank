'''
Created on May 25, 2018

@author: nishant.sethi
'''

import math
def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += bi_dist(i, n, p)   
print("%.3f" %b)