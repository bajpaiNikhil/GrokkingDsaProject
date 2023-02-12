

"""

Approach 1 using brute force
import math
nums = [-1]
k = 1
maxSum = -math.inf
a = k
for i in range(0,len(nums)):
    if k > len(nums):
        break
    maxSum = max(maxSum , sum(nums[i:k]))
    k+=1
w = (maxSum/a)
print('%.5f'% w)

"""


"""
Approach 2 - using sliding window

"""
import math
nums = [2,1,5,1,3,2]
k=3
windowSum = 0
windowStart = 0
maxSum = -math.inf
for i in range(len(nums)):
    windowSum += nums[i]
    print(i,k,windowSum,windowStart,maxSum)
    if i >=k-1:
        #print("here",i, k, windowSum, windowStart, maxSum)
        maxSum=max(windowSum,maxSum)
        windowSum-=nums[windowStart]
        windowStart+=1
        print("here", i, k, windowSum, windowStart, maxSum)
print(maxSum)
















