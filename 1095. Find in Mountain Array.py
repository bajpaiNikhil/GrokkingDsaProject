def findMax(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


def binarySearchOnArray(arr, key, start, end):
    # print(left,right)
    while start <= end:
        mid = start + (end - start) // 2
        # print(left,right,mid)

        if key == arr[mid]:
            return key
        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


nums = [1, 3, 8, 4, 3]
key = 4
maxIndex = findMax(nums)
print(maxIndex)
keyIndex = binarySearchOnArray(nums, key, 0, maxIndex)
if keyIndex != -1:
    print(keyIndex)
    exit(0)
else:
    print(binarySearchOnArray(nums, key, maxIndex + 1, len(nums) - 1))
