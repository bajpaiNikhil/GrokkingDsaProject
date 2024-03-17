nums = [2,3,3,4,6,7]
target = 12
nums.sort()
left = 0
right = len(nums)-1

count = 0
mod = 10**9+7

while left<=right:
    if nums[left]+nums[right] <= target:
        count += pow(2,(right-left),mod)
        left +=1
    else:
        right-=1
print(count)
