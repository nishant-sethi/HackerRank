import numpy as np
lst=map(int,raw_input().split())
arr=np.array(lst,int)
print arr.reshape(3,3)