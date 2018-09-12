from itertools import groupby
data=input()
groups = []
uniquekeys = []
for k, g in groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
lst=[]
for i in groups:
    lst.append((len(i),int(i[0])))
for i in lst:
    print(i,end=' ')