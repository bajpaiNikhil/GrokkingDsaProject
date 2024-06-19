s = "AABABBA"
k=1
windowStart = 0
maxLengthCount = 0
maxRepeatingCharCountInHashmap = 0
hashMap = {}
for i in range(len(s)):
    hashMap[s[i]] = hashMap.get(s[i],0)+1
    maxRepeatingCharCountInHashmap = max(maxRepeatingCharCountInHashmap,hashMap[s[i]])
    # print(maxRepeatingCharCountInHashmap)
    if (i - windowStart +1) - maxRepeatingCharCountInHashmap >k:
        hashMap[s[windowStart]] -=1
        if hashMap[s[windowStart]] == 0:
            del hashMap[s[windowStart]]
        windowStart += 1
    maxLengthCount = max(maxLengthCount,i-windowStart+1)
print(maxLengthCount)
# windowStart = 0
# maxLenCount = 0
# mCharacterHashMap = {}
# maxCharacterRepeatingCount = 0
#
# for i in range(len(s)):
#     mCharacterHashMap[s[i]] = mCharacterHashMap.get(s[i],0)+1
#
#     maxCharacterRepeatingCount = max(maxCharacterRepeatingCount,mCharacterHashMap[s[i]])
#     print(maxCharacterRepeatingCount)
#     if (i-windowStart+1) - maxCharacterRepeatingCount >k:
#         mCharacterHashMap[s[windowStart]]-=1
#         if(mCharacterHashMap[s[windowStart]]) == 0:
#             del mCharacterHashMap[s[windowStart]]
#         windowStart+=1
#     maxLenCount = max(maxLenCount,i-windowStart+1)
#
# print(mCharacterHashMap,maxLenCount)
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
