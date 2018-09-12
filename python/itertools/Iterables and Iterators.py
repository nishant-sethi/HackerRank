from itertools import combinations
n=int(input())
letters=[x for x in input().split()]
k=int(input())
res=list(combinations(letters,k))
count=0
for i in res:
    if 'a' in i:
        count+=1
print(count/len(res))