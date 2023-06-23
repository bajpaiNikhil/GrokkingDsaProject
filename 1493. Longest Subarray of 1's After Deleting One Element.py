nums = [1,1,1]

windowStart = 0
maxWindowCount = 0
maxCharacterCount = 0

if len(set(nums)) == 1:
    print("1",len(nums) - 1)
for windowEnd in range(len(nums)):
    if nums[windowEnd] == 1:
        maxCharacterCount += 1
    if windowEnd - windowStart + 1 - maxCharacterCount > 1:
        if nums[windowStart] == 1:
            maxCharacterCount -= 1
        windowStart+=1
    maxWindowCount = max(maxCharacterCount,maxWindowCount)
print("2",maxWindowCount)
