finalList = []


def printSubsetSum(i, n, arr, l, target):
    if target == 0:
        finalList.append(l[:])
        return
    if target < 0:
        return
    if i == n:
        return
    printSubsetSum(i + 1, n, arr, l, target)
    l.append(arr[i])
    printSubsetSum(i, n, arr, l, target - arr[i])
    l.pop()


nums = [2, 3, 5]
print(printSubsetSum(0, len(nums), nums, [], 8))
print(finalList)
