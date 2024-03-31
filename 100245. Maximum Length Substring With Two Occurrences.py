
# Example usage
s = "aaaa"
d = {}
windowStart = 0
maxSize = 0
for windowEnd in range(len(s)):
    if s[windowEnd] not in d:
        d[s[windowEnd]] = 0
    d[s[windowEnd]]+=1

    while d[s[windowEnd]] > 2:
        d[s[windowStart]]-=1
        windowStart+=1
        if d[s[windowStart]] == 0:
            del d[s[windowStart]]
    maxSize = max(maxSize,windowEnd-windowStart+1)
print(maxSize)