import math

s = "araaci"
k = 2


windowHashMap = {}
windowStart = 0
windowLen = 0
maxSize = 0
res = ""
for i in range(len(s)):
    windowHashMap[s[i]] = windowHashMap.get(s[i],0)+1
    res+=s[i]
    while len(windowHashMap)>k:
        windowHashMap[s[windowStart]] -=1
        if windowHashMap[s[windowStart]] == 0:
            del windowHashMap[s[windowStart]]
        windowStart+=1
    maxSize = max(maxSize,i-windowStart+1)
print(windowHashMap,maxSize)


# windowStart = 0
# maxSize = -math.inf
# hashSet = {}
# for i in range(len(s)):
#     if s[i] not in hashSet:
#         hashSet[s[i]] = 1
#     else:
#         hashSet[s[i]] += 1
#     #(hashSet)
#     while len(hashSet) > k:
#         hashSet[s[windowStart]]-=1
#         if hashSet[s[windowStart]]==0:
#             del hashSet[s[windowStart]]
#         windowStart+=1
#     maxSize = max(maxSize,i-windowStart+1)
#     #print(max(maxSize,i-windowStart+1),maxSize,i,windowStart+1)
# print(maxSize if len(hashSet)==k else -1)
# a = int(input())
# print(a)