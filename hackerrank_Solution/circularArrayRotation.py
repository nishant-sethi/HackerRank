length, ops, qs = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

delta = ops % length

for _ in range(qs):
    index = int(input())
    print(nums[index - delta])
    
