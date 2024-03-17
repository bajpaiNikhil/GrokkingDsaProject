import math

nums = [1,5,4,2,9,9,9]
k = 3

wSet = set()
wSum = 0
wStart = 0
maxSum= -math.inf
for wEnd in range(len(nums)):
    while nums[wEnd] in wSet or len(wSet)== k:
        wSet.remove(nums[wStart])
        wSum-=nums[wStart]
        wStart+=1
    wSum +=nums[wEnd]
    wSet.add(nums[wEnd])
    # print(wSet)
    if len(wSet)== k:
        # print(maxSum,wSet,wSum)
        maxSum = max(wSum,maxSum)
print(maxSum)
