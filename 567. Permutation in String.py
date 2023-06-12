import collections
import math

s = "ab"
p = "a"
D = math.inf
d = {}
windowStart = 0
found = 0

for i in p:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] -= 1
        if d[s[i]] == 0:
            found += 1
    if found == len(d):
        print("True")
        break
    if i > len(p) - 1:
        if s[windowStart] in d:
            if d[s[windowStart]] == 0:
                found -= 1
            d[s[windowStart]] += 1
        windowStart+=1
print(False)

