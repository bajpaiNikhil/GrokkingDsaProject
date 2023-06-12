s = "xyzzaz"
k = 3
sSet = set()
windowStart = 0
count = 0
for i in range(len(s)):
    while s[i] in sSet:
        sSet.remove(s[windowStart])
        windowStart += 1
    sSet.add(s[i])
    if len(sSet) > k:
        sSet.remove(s[windowStart])
        windowStart += 1
    if len(sSet) == k:
        count += 1
print(count)
