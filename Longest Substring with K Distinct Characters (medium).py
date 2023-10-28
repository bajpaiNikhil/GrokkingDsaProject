import math

s = "abcbbc"
k = 2

windowStart = 0
maxSize = -math.inf
hashSet = {}
for i in range(len(s)):
    if s[i] not in hashSet:
        hashSet[s[i]] = 1
    else:
        hashSet[s[i]] += 1
    #(hashSet)
    while len(hashSet) > k:
        hashSet[s[windowStart]]-=1
        if hashSet[s[windowStart]]==0:
            del hashSet[s[windowStart]]
        windowStart+=1
    maxSize = max(maxSize,i-windowStart+1)
    #print(max(maxSize,i-windowStart+1),maxSize,i,windowStart+1)
print(maxSize if len(hashSet)==k else -1)
a = int(input())
print(a)