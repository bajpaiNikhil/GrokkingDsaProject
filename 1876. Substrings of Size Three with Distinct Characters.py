

s = "abcabc"
windowStart = 0
count = 0
S = set()
k = 3
for i in range(len(s)):
    while s[i] in S:
        S.remove(s[windowStart])
        S.remove("3")
        windowStart+=1
    S.add(s[i])
    if len(S)> 3:
        S.remove(s[windowStart])
        windowStart+=1
    if len(S) == k:
        count+=1
    print(S)
print(count)

