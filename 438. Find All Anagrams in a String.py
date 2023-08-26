

s = "cbaebabacd"
p = "abc"

windowStart = 0
pCount = {}
sCount = {}

for i in range(len(p)):
    pCount[p[i]] = 1 + pCount.get(p[i],0)
    sCount[s[i]] = 1 + sCount.get(s[i], 0)
result = [0] if sCount == pCount else []
print(pCount)
for windowEnd in range(len(p), len(s)):
    sCount[s[windowEnd]] = 1 + sCount.get(s[windowEnd],0)
    sCount[s[windowStart]] -= 1
    if sCount[s[windowStart]] == 0:
        sCount.pop(s[windowStart])
    windowStart+=1
    if sCount == pCount:
        result.append(windowStart)
print(result)




