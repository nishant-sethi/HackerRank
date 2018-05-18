import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    _list=ar
    _list[k]=0
    summ=sum(_list)
    if summ//2 == b:
        return "Bon Appetit"
    else:
        return b- summ//2

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)