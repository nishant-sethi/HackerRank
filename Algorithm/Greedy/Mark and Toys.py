n,k=map(int,input().split())
nums=[int(x) for x in input().split()]
c=0
sum=0
for i in sorted(nums):
    sum+=i
    c+=1
    if sum>k:
        c-=1
        break     
print(c)