

Fruit=[0,1,2,2]
target = 2

fruitHashMap = {}
windowStart = 0
maxFruitCount = 0

for i in range(len(Fruit)):
    fruitHashMap[Fruit[i]] = fruitHashMap.get(Fruit[i],0)+1

    while len(fruitHashMap)>2:
        fruitHashMap[Fruit[windowStart]] -=1
        if fruitHashMap[Fruit[windowStart]] == 0:
            del fruitHashMap[Fruit[windowStart]]
        windowStart+=1
    maxFruitCount = max(maxFruitCount,i-windowStart+1)
print(fruitHashMap,maxFruitCount)



# hashSet = {}
# windowStart = 0
# maxCount = 0
#
# for i in range(len(Fruit)):
#     if Fruit[i] not in hashSet:
#         hashSet[Fruit[i]]=1
#     else :
#         hashSet[Fruit[i]]+=1
#     # print(hashSet)
#
#     while len(hashSet)>target:
#         hashSet[Fruit[windowStart]]-=1
#         if hashSet[Fruit[windowStart]] ==0:
#             del hashSet[Fruit[windowStart]]
#         windowStart += 1
#     maxCount = max(maxCount , i-windowStart+1)
# print(maxCount)
