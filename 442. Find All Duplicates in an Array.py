nums = [4, 3, 2, 7, 8, 2, 3, 1]
i = 0
while i < len(nums):
    j = nums[i] - 1
    # print(j,j+1, nums[i],i,nums)
    if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
    else:
        i += 1
print(nums)
dN = []
for i in range(len(nums)):
    if nums[i] != i+1 :
        dN.append(nums[i])
print(dN)