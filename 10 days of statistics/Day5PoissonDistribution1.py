'''
Created on May 28, 2018

@author: nishant.sethi
'''

import math
k=5
lamda=2.5
result=((lamda**k)*(math.exp(-lamda)))/math.factorial(k)
print(round(result,3))