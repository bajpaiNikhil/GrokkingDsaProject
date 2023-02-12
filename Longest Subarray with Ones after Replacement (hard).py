arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
windowStart = 0
maxCount = 0
hashMap = {}
maxCharacterCount = 0
for i in range(len(arr)):
    if arr[i] == 1:
        maxCharacterCount += 1
    if i - windowStart + 1 - maxCharacterCount > k:
        if arr[windowStart] == 1:
            maxCharacterCount -= 1
        windowStart += 1
    maxCount = max(maxCount, i - windowStart + 1)
print(maxCount)
