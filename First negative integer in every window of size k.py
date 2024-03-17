K = 2
nums = [-8, 2, 3, -6, 10]

# l = 0
# r = 0
# temp_store = []
# final_ans = []
# while r < len(arr):
#     if arr[r] < 0:
#         temp_store.append(arr[r])
#
#     if r - l + 1 != k:
#         r += 1
#     elif r - l + 1 == k:
#         if len(temp_store) == 0:
#             final_ans.append(0)
#         else:
#             final_ans.append(temp_store[0])
#             if arr[l] < 0:
#                 temp_store.pop(0)
#         r += 1
#         l += 1
# print(final_ans)
tempList = []
finalList = []
wStart = 0

for wEnd in range(len(nums)):
    if nums[wEnd] < 0:
        tempList.append(nums[wEnd])
    if wEnd - wStart + 1 == K:
        if len(tempList) == 0:
            finalList.append(0)
        else:
            finalList.append(tempList[0])
            if nums[wStart] < 0:
                tempList.pop(0)
        wStart += 1

print(finalList)
