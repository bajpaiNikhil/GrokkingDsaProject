import math

chalk = [3, 4, 1, 2]
k = 25

prefixSumArray = [chalk[0]]
for i in range(1, len(chalk)):
    prefixSumArray.append(chalk[i] + prefixSumArray[-1])
print(prefixSumArray)
remainingChalk = k % prefixSumArray[-1]
# print(remainingChalk)
left = 0
right = len(prefixSumArray) - 1
while left <= right:
    mid = left + (right - left) // 2
    if prefixSumArray[mid] > remainingChalk:
        right = mid - 1
    else:
        left = mid + 1
print(left)
