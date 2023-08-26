import math

nums = [1]
m = 1
windowStart = 0
windowSum = 0
isTrueFlag = False
minLength = math.inf
for windowEnd in range(len(nums)):
    windowSum += nums[windowEnd]
    while windowSum>=m:
        # print(windowSum,"this is it")
        minLength = min(minLength,windowEnd-windowStart+1)
        print(minLength)
        windowSum-=nums[windowStart]
        windowStart+=1
print(minLength)
if minLength!=len(nums):
    print(True)
else:
    print(False)
