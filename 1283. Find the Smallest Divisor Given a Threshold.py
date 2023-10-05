import math

nums = [44,22,33,11,1]
threshold = 5

left = 1
right = max(nums)
ans = 0

def check(nums,mid , h):
    return sum(math.ceil(num / mid) for num in nums) <= h


while left <= right:
    mid = left + (right - left) // 2
    if check(nums, mid , threshold):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
