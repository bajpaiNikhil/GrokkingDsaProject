import math

target = 7
nums = [2, 3, 1, 2, 4, 3]

windowSum = 0
windowStart = 0
minSize = math.inf

for i in range(len(nums)):
    windowSum += nums[i]
    while windowSum >= target:
        minSize = min(minSize, i - windowStart + 1)
        windowSum -= nums[windowStart]
        windowStart += 1
print(0 if minSize == math.inf else minSize )
