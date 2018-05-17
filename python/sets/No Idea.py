n,m=map(int,raw_input().split())
arr=map(int,raw_input().split())
a=set(map(int,raw_input().split()))
b=set(map(int,raw_input().split()))
happiness=0
for i in arr:
    if i in a:
        happiness+=1
    if i in b:
        happiness-=1
print happiness