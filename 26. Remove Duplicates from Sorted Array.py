


nums = [0,0,1,1,1,2,2,3,3,4]

nextDuplicate = 1

i = 1
while i <len(nums):
    if nums[nextDuplicate-1] != nums[i]:
        nums[nextDuplicate] = nums[i]
        nextDuplicate+=1
    i+=1
print(nextDuplicate,len(set(nums)))
