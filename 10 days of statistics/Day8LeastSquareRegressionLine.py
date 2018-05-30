'''
Created on May 29, 2018

@author: nishant.sethi
'''
import math
def std(x):
    num_items = len(x)
    mean = sum(x) / num_items
    differences = [x - mean for x in x]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    sd = math.sqrt(variance)
    return sd
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
x=[]
y=[]
for i in range(5):
    a,b=input().split()
    x.append(int(a))
    y.append(int(b)) 
coff=corrCof(x, y)
std_x=std(x)
std_y=std(y)
b=(coff*std_y)/std_x
mean_x=sum(x)/len(x)
mean_y=sum(y)/len(y)
a=mean_y-b*mean_x
x=80
y=a+x*b
print(round(y,3)) 