


s = "aabccbb"

windowStart = 0
maxSize = 0
hashSet = set()

for i in range(len(s)):
    while s[i] in hashSet:
        hashSet.remove(s[windowStart])
        windowStart+=1
    hashSet.add(s[i])
    maxSize = max(maxSize  , i-windowStart+1)
print(maxSize)

