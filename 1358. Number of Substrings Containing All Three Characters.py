s = "abcabc"

windowStart = 0
hashMap = {}
count = 0
for windowEnd in range(len(s)):
    if s[windowEnd] not in hashMap:
        hashMap[s[windowEnd]] = 0
    hashMap[s[windowEnd]]+=1
