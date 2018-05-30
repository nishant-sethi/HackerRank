'''
Created on May 30, 2018

@author: nishant.sethi
'''
from sklearn import linear_model    
m,n=input().split()
m=int(m)
n=int(n)
x_train=[]
y_train=[]
x_test=[]
for i in range(n):
    x=[float(a) for a in input().split()]
    x_train.append(x[0:m])
    y_train.append(x[m])
n_t=int(input())
for i in range(n_t):
    x=[float(a) for a in input().split()]
    x_test.append(x)
model=linear_model.LinearRegression()
model.fit(x_train, y_train) 
a=model.intercept_
b=model.coef_
result=model.predict(x_test)
for i in result:
    print(round(i,2))