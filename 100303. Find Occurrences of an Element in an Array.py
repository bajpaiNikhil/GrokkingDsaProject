nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
listDict = {}
res = []

for i in range(len(nums)):
    if nums[i] not in listDict:
        listDict[nums[i]] = []

    listDict[nums[i]].append(i)
# print(listDict)
if x in listDict:
    occurrences = listDict[x]
else:
    occurrences = []
for k in queries:
    if k <= len(occurrences):
        res.append(occurrences[k - 1])
    else:
        res.append(-1)
print(res)
