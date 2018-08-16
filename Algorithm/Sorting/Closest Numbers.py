n =  input()
nums = list(map(int,input().strip().split()))
nums.sort()
lowestDiff = nums[1]-nums[0]
res = [nums[0],nums[1]]
for i in range(1,len(nums)-1):            
    if nums[i+1]-nums[i] < lowestDiff:
        res = []   
        res.append(nums[i])
        res.append(nums[i+1])
        lowestDiff = abs(nums[i+1]-nums[i])
    elif nums[i+1]-nums[i] == lowestDiff:
        res.append(nums[i])
        res.append(nums[i+1])

print(*res)