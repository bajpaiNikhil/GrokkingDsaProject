import math

# nums = [1, 2, 3]
# finalList = []


# def getSetBit(num, bit):
#     temp = 1 << bit
#     # print("temp", temp)
#     temp = temp & num
#     # print("temp after and ", temp)
#
#     if temp == 0:
#         return 0
#     else:
#         return 1
#
#
# if len(nums) != 0:
#     subsetCount = int(math.pow(2, len(nums)))
#     # print(subsetCount)
#     for i in range(0, subsetCount):
#         # print(i)
#         subList = []
#         for j in range(0, len(nums)):
#             # print(i,j,nums[j],getSetBit(i,j))
#             if getSetBit(i, j) == 1:
#                 subList.append(nums[j])
#         finalList.append(subList)
#     print(finalList)
# else:
#     print([])

# # below approach is using backtracking
# def printAllSubset(i, n, arr, l):
#     if i == n:
#         finalList.append(l[:])  # Append a copy of the list
#         return
#
#         # Include the current element
#     l.append(arr[i])
#     printAllSubset(i + 1, n, arr, l)
#
#     # Exclude the current element
#     l.pop()  # Remove the last element
#     printAllSubset(i + 1, n, arr, l)
#     return finalList


# print(printAllSubset(0, 3, nums, []))


nums = [2, 5, 7]
parentSubsetList = []


def getSetBit(subsetInt, bitPosition):
    temp = 1 << bitPosition  # Create a mask for the bit at 'bitPosition'
    temp = temp & subsetInt  # Check if the bit is set in the subsetInt
    if temp == 0:
        return 0
    else:
        return 1


subsetCount = int(math.pow(2, len(nums)))  # Total subsets = 2^n
for i in range(subsetCount):  # Iterate over all possible subsets
    subset = []
    for j in range(len(nums)):  # Iterate over each bit position
        if getSetBit(i, j) == 1:  # Check if the j-th bit in i is set
            subset.append(nums[j])  # Include nums[j] in the subset
    parentSubsetList.append(subset)  # Add the subset to the result list

print(parentSubsetList)
