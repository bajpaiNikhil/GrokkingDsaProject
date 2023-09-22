
# "abcd"
# "cdef"
# 1

s = "abcd"
t = "cdef"
maxCost = 1
currentCost = 0
maxWindowLength = 0
windowStart = 0

for windowEnd in range(len(s)):
    currentCost += abs(ord(s[windowEnd]) - ord(t[windowEnd]))
    print(currentCost)
    while currentCost> maxCost:
        currentCost -= abs(ord(s[windowStart]) - ord(t[windowStart]))
        print(s[windowStart],ord(s[windowStart]),t[windowStart],ord(t[windowStart]) ,abs(ord(s[windowStart]) - ord(t[windowStart])))
        windowStart+=1
    maxWindowLength = max(windowEnd-windowStart+1 , maxWindowLength)
print(maxWindowLength)
