strs = ["eat","tea","tan","ate","nat","bat"]


strDict = {}
for i in strs:
    sortedString = "".join(sorted(i))
    print(sortedString)
    if sortedString not in strDict:
        strDict[sortedString] = []
    strDict[sortedString] += [i]
print(list(strDict.values()))