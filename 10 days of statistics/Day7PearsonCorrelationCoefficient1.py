'''
Created on May 29, 2018

@author: nishant.sethi
'''
import math

def corrCof(x,y):
    result=cov(x,y)/(std(x)*std(y))
    return round(result,3) 

def cov(x,y):
    mean_x=sum(x)/len(x)
    mean_y=sum(y)/len(y)
    result=0
    for i in range(len(x)):
        result+=(x[i]-mean_x)*(y[i]-mean_y)
    return result/len(x) 
def std(x):
    num_items = len(x)
    mean = sum(x) / num_items
    differences = [x - mean for x in x]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    sd = math.sqrt(variance)
    return sd

n=int(input())
X=[float(x) for x in input().split()]
Y=[float(x) for x in input().split()]
print(corrCof(X,Y))