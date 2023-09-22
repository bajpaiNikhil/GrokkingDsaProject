



nums = [1,3,5,2,1,3,1]

currentGreatness = 0

nums.sort()
for i in nums:
    if i > nums[currentGreatness]:
        currentGreatness+=1
print(currentGreatness)