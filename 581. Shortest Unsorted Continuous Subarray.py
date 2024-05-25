import math

nums = [1, 3, 2, 2, 2]

low = 0
high = len(nums) - 1

while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
    low += 1
if low == len(nums) - 1:
    print(0)
while high > 0 and nums[high] >= nums[high - 1]:
    high -= 1
print(low, high, nums[low:high + 1])

subArray_max = -math.inf
subArray_min = math.inf

for i in range(low, high + 1):
    subArray_max = max(subArray_max, nums[i])
    subArray_min = min(subArray_min, nums[i])

print(subArray_min, subArray_max)

while low > 0 and nums[low - 1] > subArray_min:
    low -= 1
while high > 0 and nums[high + 1] < subArray_min:
    high += 1
print(high - low + 1)
