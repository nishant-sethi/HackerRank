import numpy as np
inp1=[]
inp2=[]
n,m,p=map(int,raw_input().split())
for i in range(0,n):
    lst=map(int,raw_input().split())
    inp1.append(lst)
for i in range(0,m):
    lst=map(int,raw_input().split())
    inp2.append(lst)
arr1=np.array(inp1,int)
arr2=np.array(inp2,int)
print np.concatenate((arr1, arr2),axis=0)  