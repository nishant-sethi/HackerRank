n,d=[int(x)for x in input().split(" ")]
arr=list(map(int,input().split(" ")))
gc=0;
for i in range(n):
    if arr[i]+d in arr and arr[i]+2*d in arr:
        gc+=1
print (gc)

