from itertools import combinations
x,y=input().split()
res=[]
for i in range(1,int(y)+1):
    res.append(list(combinations(x,i)))
lst=[]
for i in res:
    lst1=[]
    for j in i:
        x=''.join(sorted(j))
        lst1.append(x)
        lst1.sort()
    lst.append(lst1)
for i in lst:
    for j in i:
        print(j)