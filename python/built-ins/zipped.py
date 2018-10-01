n,x=map(int,input().split())
res=[]
for i in range(x):
    nums=[float(x) for x in input().split()]
    res.append(nums)
for i in (zip(*res)):
    print(round(sum(i)/x,1))