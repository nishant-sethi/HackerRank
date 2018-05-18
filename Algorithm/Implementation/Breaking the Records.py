import sys

def getRecord(s):
    # Complete this function
    new_list=s[0:1]
    best=0
    worst=0
    x=min(new_list)
    y=max(new_list)
    for i in range(2,len(s)+1):
        new_list=s[0:i]
        new_x=min(new_list)
        new_y=max(new_list)
        if new_x in new_list and x!=new_x:
            worst=worst+1
            x=new_x
        if new_y in new_list and y!=new_y:
            best=best+1
            y=new_y
    return (best,worst)


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))