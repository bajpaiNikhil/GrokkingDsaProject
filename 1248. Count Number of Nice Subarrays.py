nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

#Subarrays with exactly K odd numbers  = Subarrays with at most K odd numbers  - Subarrays with at most K-1 odd numbers

def countExactlyK(nums,A):
    windowStart = 0
    windowEnd = 0
    countForOdds = 0
    windowCount = 0
    while windowStart<len(nums):
        if nums[windowStart]&1 != 0:
            countForOdds+=1

        if countForOdds>A :
            while countForOdds>A:
                if nums[windowEnd]&1 != 0:
                    countForOdds-=1
                windowEnd+=1
        windowCount += windowStart-windowEnd +1
        windowStart+=1
    return windowCount
print(countExactlyK(nums, k) - countExactlyK(nums,k-1) )




