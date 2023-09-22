from typing import List


def longestNiceSubarray(nums: List[int]) -> int:
    windowStart = 0
    bitUnion = 0 
    maxWindowSize = 0
    for windowEnd in range(len(nums)):
        while bitUnion & nums[windowEnd] != 0 :
            bitUnion ^= nums[windowStart]
            windowStart+=1
        bitUnion |= nums[windowEnd]
        maxWindowSize = max(windowEnd - windowStart +1 , maxWindowSize)
    return maxWindowSize

nums = [1,3,8,48,10]
# nums = [744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
print(longestNiceSubarray(nums))