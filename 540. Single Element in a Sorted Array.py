
nums =[1, 1, 2]
num1, num2, num3 = nums
print(num1)
left = 0
right = len(nums) - 1

if len(nums) == 1:
    print(nums[0])
if nums[right ] <nums[right-2]:
    print(len(nums)-1)
left = 1
right = len(nums)-2

while left <= right:
    mid = left + (right - left) // 2
    if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
        print(nums[mid])
        break
    elif nums[mid] == nums[mid^1]:
        left =  mid +1
    else:
        right = mid-1
print(-1)

# xor = 0
#
# for i in nums:
#     xor^=i
# print(xor)
