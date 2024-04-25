finalList = []


def combinationSumII(i, n, arr, target, l):
    if target == 0:
        finalList.append(l[:])
        return
    if i == n:
        return
    if target < 0:
        return
    l.append(arr[i])
    combinationSumII(i + 1, n, arr, target - arr[i], l)
    l.pop()
    while i + 1 < n and arr[i + 1] == arr[i]:
        i += 1
    combinationSumII(i+1, n, arr, target, l)


nums = [10, 1, 2, 7, 6, 1, 5]
nums.sort()
combinationSumII(0, len(nums), nums, 8, [])
print(finalList)
