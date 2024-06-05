nums = [1, 3, 8, 10, 15]
key = 12

left = 0
right = len(nums) - 1

while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == key:
        print(nums[mid])
        exit(0)
    elif nums[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
print(left,right)
# After the loop, left is the smallest index greater than key, right is the largest index less than key
# To handle edge cases where left or right is out of bounds
if left >= len(nums):
    print(nums[right])
elif right < 0:
    print(nums[left])
else:
    if (nums[left] - key) < (key - nums[right]):
        print(nums[left])
    else:
        print(nums[right])
