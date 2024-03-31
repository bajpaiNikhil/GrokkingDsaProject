import math

nums = [16,1,2,20,32]

k = 45

windowStart = 0
windowSize = math.inf
# for windowEnd in range(len(nums)):
#     windowOr |= nums[windowEnd]
#
#     while windowOr >= k :
#         windowSize = min(windowSize , windowEnd-windowStart+1)
#         windowOr^= nums[windowStart]
#         windowStart+=1
print(windowSize)

windowSize = math.inf
for windowStart in range(len(nums)):
    windowOR = 0

    for windowEnd in range(windowStart,len(nums)):
        windowOR =  windowOR | nums[windowEnd]
        if windowOR >=k:
            windowSize= min(windowSize, windowEnd-windowStart+1)
print(windowSize)
