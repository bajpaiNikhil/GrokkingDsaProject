finalList = set()


def printAllSubsetII(i, n, arr, l):
    if i == n:
        finalList.add(tuple(l))
        return
    l.append(nums[i])
    printAllSubsetII(i + 1, n, arr, l[:])
    l.pop()
    while i + 1 < n and nums[i] == nums[i + 1]:
        i += 1
    printAllSubsetII(i + 1, n, arr, l[:])
    return finalList


# Skip over consecutive duplicates to avoid generating duplicate subsets
nums = [4, 4, 4, 1, 4]
nums.sort()
print(printAllSubsetII(0, len(nums), nums, []))
uniqueList = []
for i in finalList:
    uniqueList.append(list(i))
print(uniqueList)
