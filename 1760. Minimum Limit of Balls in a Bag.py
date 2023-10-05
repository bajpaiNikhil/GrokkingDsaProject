nums = [2, 4, 8, 2]
maxOperations = 4


def check(nums, mid, maxOperations):
    return sum((n - 1) // mid for n in nums) > maxOperations


left = 1
right = max(nums)
ans = 0
while left <= right:
    mid = left + (right - left) // 2

    if check(nums, mid, maxOperations):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
