nums = [1, 2, 3, 2, 3, 4, 5]
xor = 0
sameDict = {}

for i in nums:
    sameDict[i] = sameDict.get(i, 0) + 1
# print(sameDict)
# print(xor)

for key, val in sameDict.items():
    if val == 2:
        xor ^= key
print(xor)
