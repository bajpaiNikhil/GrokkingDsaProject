import math

nums = [9,4,1,7]
k = 2
nums.sort()
print(nums)
minVal = nums[k-1]-nums[0]
for windowEnd in range(k,len(nums)):
    minVal = min(minVal , nums[windowEnd]-nums[windowEnd-k+1])
print(minVal)