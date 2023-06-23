answerKey = "TFFT"
k = 1

windowStart = 0
maxCount = 0
maxCharacterCount = 0
hashMap = {}
for windowEnd in range(len(answerKey)):
    if answerKey[windowEnd] not in hashMap:
        hashMap[answerKey[windowEnd]] = 0
    hashMap[answerKey[windowEnd]] += 1
    maxCharacterCount = max(maxCharacterCount, hashMap[answerKey[windowEnd]])

    if (windowEnd - windowStart + 1) - maxCharacterCount > k:
        hashMap[answerKey[windowStart]] -= 1
        if hashMap[answerKey[windowEnd]] == 0:
            del hashMap[answerKey[windowEnd]]
        windowStart += 1
    maxCount = max(windowEnd-windowStart + 1, maxCount)
print(maxCount)
