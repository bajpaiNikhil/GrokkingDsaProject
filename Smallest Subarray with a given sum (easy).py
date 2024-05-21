import math

nums = [2, 1, 5, 2, 3, 2]
s = 7

windowStart = 0
windowSize = math.inf
windowSum = 0

for i in range(len(nums)):
    windowSum += nums[i]
    while windowSum >= s:
        windowSize = min(i - windowStart + 1, windowSize)
        windowSum -= nums[windowStart]
        windowStart += 1
print(windowSize)
