

Fruit=[0,1,2,2]
target = 2
hashSet = {}
windowStart = 0
maxCount = 0

for i in range(len(Fruit)):
    if Fruit[i] not in hashSet:
        hashSet[Fruit[i]]=1
    else :
        hashSet[Fruit[i]]+=1
    # print(hashSet)

    while len(hashSet)>target:
        hashSet[Fruit[windowStart]]-=1
        if hashSet[Fruit[windowStart]] ==0:
            del hashSet[Fruit[windowStart]]
        windowStart += 1
    maxCount = max(maxCount , i-windowStart+1)
print(maxCount)
