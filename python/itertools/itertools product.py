from itertools import product
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
x=(list(product(a,b)))
for i in x:
    print(i,end=' ')