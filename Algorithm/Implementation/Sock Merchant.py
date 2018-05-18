import sys

def sockMerchant(n, ar):
    # Complete this function
    count=0
    x=set(ar)
    for i in x:
        count=count+ar.count(i)//2
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)