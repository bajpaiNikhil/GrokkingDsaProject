
nums = [0,1,0,3,12]
zeroLimit = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[zeroLimit],nums[i] = nums[i],nums[zeroLimit]
        zeroLimit+=1
print(nums)