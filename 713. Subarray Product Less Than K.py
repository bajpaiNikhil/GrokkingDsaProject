from collections import deque

nums = [10,5,2,6]
target =100

res = []
product = 1
left = 0
count = 0
for right in range(len(nums)):
    product *= nums[right]
    while product >= target and left<= right:
        print("2", left, right,product)

        product//=nums[left]
        left+=1
    tempList = deque()
    count+=right-left+1
    print("here" , count)
    for i in range(right,left-1,-1):
        print("this",right , left, i , nums[i])
        tempList.appendleft(nums[i])
        res.append(list(tempList))

print(res)