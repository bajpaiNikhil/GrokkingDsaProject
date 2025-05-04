cardPoints = [1,1000,1]
k = 1

# prefixSumArray = [cardPoints[0]]
#
# for i in range(1,len(cardPoints)-1):
#     prefixSumArray.append(prefixSumArray[i-1]+cardPoints[i])
# print(prefixSumArray)

totalSum = sum(cardPoints)
windowStart = 0
windowSize = len(cardPoints)-k
windowSum = sum(cardPoints[:windowSize])
minWindow = windowSum
if k == len(cardPoints):
    print(sum(cardPoints))
    exit(0)
for i in range(windowSize, len(cardPoints)):
    windowSum += cardPoints[i] - cardPoints[i-windowSize]
    minWindow = min(minWindow,windowSum)
print(minWindow)

print(totalSum-minWindow)