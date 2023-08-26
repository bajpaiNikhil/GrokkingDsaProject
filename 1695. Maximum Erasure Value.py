

nums = [5,2,1,2,5,2,1,2,5]

hashSet = set()
windowStart = 0
windowSum = 0
maxSum =  0
for windowEnd in nums:
    while windowEnd in hashSet:
        windowSum-=nums[windowStart]
        hashSet.remove(nums[windowStart])
        windowStart+=1
    windowSum+= windowEnd
    hashSet.add(windowEnd)
    maxSum = max(windowSum,maxSum)
print(maxSum,hashSet)


