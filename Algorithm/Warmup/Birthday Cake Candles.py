import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    x=max(ar)
    count=0
    for i in ar:
        if i == x:
            count=count+1
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)