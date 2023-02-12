


s = "AAAA"
k = 0
windowStart = 0
maxCount = 0
hashMap = {}
maxCharacterCount = 0
for i in range(len(s)):
    if s[i] not in hashMap:
        hashMap[s[i]] = 1
    else:
        hashMap[s[i]]+=1
    maxCharacterCount = max(maxCharacterCount , hashMap[s[i]])

    if ((i-windowStart + 1 ) - maxCharacterCount) > k:
        hashMap[s[windowStart]] -=1
        windowStart+=1
    maxCount = max(maxCount , i - windowStart+1)
print(maxCount)
