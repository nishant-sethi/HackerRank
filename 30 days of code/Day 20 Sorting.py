
import sys
def bubbleSort(arr):
    n = len(arr)
    count=0
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count+=1
    return (arr,count)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
result=bubbleSort(a)
print("Array is sorted in",result[1],"swaps.")
print("First Element:",result[0][0])
print("Last Element:",result[0][len(a)-1])