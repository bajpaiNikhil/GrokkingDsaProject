

nums = [3,5,4,2,4,6]

nums.sort()

leftPointer = 0
rightPointer = len(nums)-1
sumIs = -1
while leftPointer<rightPointer:
    sumIs = max(sumIs,nums[leftPointer]+nums[rightPointer])
    leftPointer+=1
    rightPointer-=1
print(sumIs)