nums = [7, 8, 3, 4, 15, 13, 4, 1]
nums.sort()
average = []
print(nums)
left = 0
right = len(nums)-1
count = 0
while count < len(nums)//2 :
    print(left,right)
    average.append((nums[left]+nums[right]) /2)
    left+=1
    right-=1
    count+=1
print(average)
