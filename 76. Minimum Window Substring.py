s = "aa"
t = "aa"

dic = {}
windowStart = 0
matched = 0
min_len = len(s) + 1
start = 0
for char in t:
    dic[char] = dic.get(char, 0) + 1

for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] -= 1
        if dic[s[i]] == 0:
            matched += 1
    # shrinking the window
    while matched == len(dic):
        if min_len > i-windowStart+1:
            min_len = i-windowStart+1
            start = windowStart

        if s[windowStart] in dic:
            if dic[s[windowStart]] == 0:
                matched-=1
            dic[s[windowStart]]+=1
        windowStart+=1

if min_len > len(s):
    print("")
print(min_len,start,s[start:start+min_len])
