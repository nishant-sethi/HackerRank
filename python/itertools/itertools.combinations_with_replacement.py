from itertools import combinations_with_replacement
x,y=input().split()
res=[]

res.append(list(combinations_with_replacement(x,int(y))))
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