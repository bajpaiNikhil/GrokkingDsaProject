nums = [1, 2, 2, 4]

i = 0
while i <len(nums):
    j = nums[i]-1
    if nums[i] != nums[j]:
        nums[i],nums[j] = nums[j],nums[i]
    else:
        i+=1
print(nums)
dN= []
for i in range(len(nums)):
    if nums[i] != i+1:
        dN.append([nums[i],i+1])
print(dN)