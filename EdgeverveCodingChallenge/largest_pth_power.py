'''
Created on Jun 1, 2018

@author: nishant.sethi
'''
import math
def isPrime(num):
    print("into prime")
    if num > 1:
        for i in range(2,int(math.sqrt(x))):
            if (num % i) == 0:
                return False
    else:
        return True
def get_power(x,n):
    p=1
    while x!=0:
        x=x//n
        p+=1
    print(p)
    return p
def find_power(x):
    if isPrime(x):
        return x
    else:
        for i in range(2,10):
            if x%i==0:
                return get_power(x,i)
            else:
                continue
x=int(input())
print(x)
res=find_power(x)
print(res)