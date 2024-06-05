


arr = [0, 2, 1, 0]
left = 0
right = len(arr)-1

while left< right:
    mid = left+(right-left)//2

    if arr[mid]> arr[mid+1]:
        right= mid
    else:
        left = mid+1
print(arr[left],left, right)