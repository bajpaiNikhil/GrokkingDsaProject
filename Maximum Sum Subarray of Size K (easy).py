nums = [2, 1, 5, 1, 3, 2]
k = 3

windowSum = 0
windowStart = 0
maxSum = 0
for i in range(len(nums)):
    windowSum+=nums[i]
    if i - windowStart +1 >=k:
        maxSum = max(maxSum,windowSum)
        windowSum-=nums[windowStart]
        windowStart+=1
print(maxSum)
