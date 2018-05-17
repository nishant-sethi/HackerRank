import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


n,r=map(int,input().split())
data=np.random.rand(r,n+1)
x=[]
for i in range(0,r):
    x=[a for a in input().split()]
    data[i]=np.array(x)
t=int(input())
test=np.random.rand(t,n)
for i in range(0,t):
    x=[a for a in input().split()]
    test[i]=np.array(x)
train=np.array(data,dtype=np.float64)
test=np.array(test,dtype=np.float64)
# train=pd.DataFrame(train)
# train.columns=["len","br","area"]
# x=train.drop("area",axis=1)
# y=train["area"]
x=train[:,0:n]
y=train[:,-1]
model=LinearRegression()
model.fit(x,y)
result=model.predict(test)
for i in result:
    print(round(i,2))