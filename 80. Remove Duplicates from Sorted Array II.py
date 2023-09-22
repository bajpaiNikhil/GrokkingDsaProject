


nums = [1,1,1,1,2,2,2,3]

slow = 2

for fast in range(2,len(nums)):

    if nums[slow-2] != nums[fast]:
        nums[slow] = nums[fast]
        slow+=1
print(slow)