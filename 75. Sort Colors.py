
nums = [2,0,1]

i = 0
low = 0
high = len(nums)-1

while i<= high:
    if nums[i] == 0:
        nums[i],nums[low] =  nums[low], nums[i]
        i+=1
        low+=1
    elif nums[i] == 1:
        i+=1
    else:
        nums[i], nums[high] = nums[high], nums[i]
        high-=1

print(nums)

