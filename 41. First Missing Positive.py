nums = [1,2,0]

i = 0
while i < len(nums):
    j = nums[i] - 1
    if 0 < nums[i] <= len(nums) and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
    else:
        i += 1
print(nums)

for i in range(len(nums)):
    if nums[i] != i + 1:
        print(i + 1)
print(len(nums)+1)
