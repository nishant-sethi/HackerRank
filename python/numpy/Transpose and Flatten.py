import numpy as np
n,m=map(int,raw_input().split())
inp=[]
for i in range(0,n):
    lst=map(int,raw_input().split())
    inp.append(lst)
arr=np.array(inp,int)
x=np.matrix(arr)
print np.transpose(x)
print arr.flatten()