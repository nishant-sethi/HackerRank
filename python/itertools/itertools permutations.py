from itertools import permutations
x,y=input().split()
res=(list(permutations(x,int(y))))
lst=[]
for i in res:
    x=''.join(i)
    lst.append(x)
lst.sort()
for i in lst:
    print(i)