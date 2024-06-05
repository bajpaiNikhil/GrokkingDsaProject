

nums = [1, 3, 8, 10, 15]
key = 200


left = 0
right = 1

while True:
    try:
        if key <= nums[right]:
            break
        newStart = right + 1
        right += (right - left + 1) * 2
        left = newStart
    except IndexError:
        break
print(left , right)
ans = -1
while left<= right:
    try:
        mid = left + (right - left) // 2
        if nums[mid] == key:
            ans = mid
            break
        elif nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    except IndexError:
        right = mid - 1
print(ans)