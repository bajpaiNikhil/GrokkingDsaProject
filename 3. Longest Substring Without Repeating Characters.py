s = "abcabcbb"

windowStart =0
windowSize = 0
maxSize =0
hashMap = {}
for i in range(len(s)):
    if s[i] in hashMap:
        windowStart = max(windowStart , hashMap[s[i]]+1)
    hashMap[s[i]] = i
    maxSize = max(maxSize,i-windowStart+1)
print(maxSize)

# windowStart = 0
# windowSize = 0
# maxSize = 0
# subStringHashMap = {}
# for i in range(len(s)):
#     if s[i] in subStringHashMap:
#         windowStart = max(windowStart, subStringHashMap[s[i]] + 1)
#     subStringHashMap[s[i]] = i
#     maxSize = max(maxSize, i - windowStart + 1)
# print(subStringHashMap, maxSize)

#
# sets = set()
# i = 0
# j = 0
# maxLength = 0
# while j <len(s):
#     if s[j] not in sets:
#         sets.add(s[j])
#         j += 1
#         maxLength = max(maxLength, j - i)
#     else:
#         sets.remove(s[i])
#         i += 1
#     # if s[j] in sets:
#     #     sets.remove(s[i])
#     #     i+=1
#     # sets.add(s[j])
#     # print(s[i:j],sets)
#     # maxLength = max(maxLength,j-i+1)
#     # j+=1
# print(maxLength)
