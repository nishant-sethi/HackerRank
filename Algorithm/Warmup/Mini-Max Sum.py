import sys

arr = map(int, raw_input().strip().split(' '))
arr.sort(cmp=None, key=None, reverse=False)
min=0
max=0
min_arr=arr[0:4]
max_arr=arr[1:5]
for i in min_arr:
    min=min+i
for i in max_arr:
    max=max+i
print(str(min)+" "+str(max))
