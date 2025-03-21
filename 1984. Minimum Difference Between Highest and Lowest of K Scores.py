import math

nums = [9,4,1,7]
k = 2
nums.sort()
min_diff = float('inf')
for i in range(len(nums)-k+1):
    # print(i,nums[i+k-1],nums[i])
    min_diff = min(min_diff,nums[i+k-1]-nums[i])
print(min_diff)
# nums.sort()
# # print(nums)
# minVal = nums[k-1]-nums[0]
# for windowEnd in range(k,len(nums)):
#     # print(windowEnd,nums[windowEnd],windowEnd-k+1)
#     minVal = min(minVal , nums[windowEnd]-nums[windowEnd-k+1])
#     print(nums[windowEnd],nums[windowEnd-k+1])
# print(minVal)