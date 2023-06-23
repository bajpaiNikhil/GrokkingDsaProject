

nums = [0,0,0,0,0,0,1,0,0,0]
goal = 0

def at_most(k , nums):
    windowStart = 0
    sumCount = 0
    windowSum = 0
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]

        while windowSum> k and windowStart <= windowEnd :
            print(nums,windowStart)
            windowSum -= nums[windowStart]
            windowStart+=1
        sumCount += windowEnd - windowStart +1
    return sumCount

print(at_most(goal,nums) - at_most(goal-1,nums))
