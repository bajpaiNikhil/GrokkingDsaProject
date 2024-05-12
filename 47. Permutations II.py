nums = [2, 2, 1, 1]
finalList = []
nums.sort()


def helper(i, arr):
    if i == len(arr):
        finalList.append(tuple(arr))
        return
    for j in range(i, len(arr)):
        # while i != j and arr[i] == arr[j]:
        #     i += 1
        if i != j and arr[j] == arr[i]:  # Skip if swapping results in duplicate permutations
            continue
        arr[i], arr[j] = arr[j], arr[i]
        helper(i + 1, arr[:])


print(helper(0, nums))
print(finalList)
result = []
for permute in finalList:
    result.append(list(permute))
print(result)
