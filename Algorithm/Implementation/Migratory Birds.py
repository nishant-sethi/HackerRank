import sys

def migratoryBirds(n, ar): 
    # Complete this function
    frequency=[0,0,0,0,0,0]
    for i in ar:
        frequency[i]=frequency[i]+1
    return frequency.index(max(frequency))

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
