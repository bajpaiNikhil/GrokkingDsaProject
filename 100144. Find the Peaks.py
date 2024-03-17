
nums = [1,1,3]
res = []
for i in range(1,len(nums)-1):
    if nums[i - 1]<nums[i] and nums[i]>nums[i + 1]:
        res.append(i)

print(res)