nums = [1, 2, 3]
finalList = []


def printAllSubset(i, n, arr, l):
    if i == n:
        finalList.append(l[:])  # Append a copy of the list
        return

        # Include the current element
    l.append(arr[i])
    printAllSubset(i + 1, n, arr, l)

    # Exclude the current element
    l.pop()  # Remove the last element
    printAllSubset(i + 1, n, arr, l)
    return finalList


print(printAllSubset(0, 3, nums, []))
