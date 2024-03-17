s = "AABABBA"
k = 1
i = 0
j = 0
maxLen = 0
maxCC = 0
d = {}
while j < len(s):
    if s[j] not in d:
        d[s[j]] = 0
    d[s[j]] += 1
    maxCC = max(maxCC, d[s[j]])
    print(d)
    if j - i + 1 - maxCC > k:
        d[s[i]] -= 1
        i += 1
    maxLen = max(maxLen, j - i + 1)
    j += 1
print(maxLen)
# windowStart = 0
# maxCount = 0
# hashMap = {}
# maxCharacterCount = 0
# for i in range(len(s)):
#     if s[i] not in hashMap:
#         hashMap[s[i]] = 1
#     else:
#         hashMap[s[i]]+=1
#     maxCharacterCount = max(maxCharacterCount , hashMap[s[i]])
#
#     if ((i-windowStart + 1 ) - maxCharacterCount) > k:
#         hashMap[s[windowStart]] -=1
#         windowStart+=1
#     maxCount = max(maxCount , i - windowStart+1)
# print(maxCount)
