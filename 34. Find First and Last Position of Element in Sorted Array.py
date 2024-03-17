nums = [5, 7, 7, 8, 8, 10]
target = 8


def binarySearchOnLeft(nums, target):
    left = 0
    right = len(nums) - 1
    ans = 0
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ans = mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(binarySearchOnLeft(nums, target))


def binarySearchOnRight(nums, target):
    left = 0
    right = len(nums) - 1
    ans = 0
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            ans = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(binarySearchOnRight(nums, target))
