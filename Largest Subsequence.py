s="abba"
count = 0
for i in range(len(s)):
    if s[i] == s[0]:
        count = max(count,i+1)
    if s[i] == s[len(s)-1]:
        count = max(count,len(s)-i)
print(count)
