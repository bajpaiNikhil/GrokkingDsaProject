txt = "cbaebabacd"
pat = "abc"
n = len(pat)
i = 0
j = 0
ans = 0
l= []
dp = {}
for char in pat:
    if char not in dp:
        dp[char] = 0
    dp[char] += 1
print(dp)
count = len(dp)
while j < len(txt):
    if txt[j] in dp:
        dp[txt[j]] -= 1
        if dp[txt[j]] == 0:
            count -= 1
    if j - i + 1 < n :
        j += 1
    else :
        if count == 0:
            ans += 1
            l.append(i)

        if txt[i] in dp:
            dp[txt[i]] += 1
            if dp[txt[i]] == 1:
                count += 1

        i += 1
        j += 1
print(ans)
print(l)
#
# string = "forxxorfxdofr"
# ptr = "for"
# n = len(string)
# k = len(ptr)
# d = {}
# for i in ptr:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# i = 0
# j = 0
# count = len(d)
#
# ans = 0
#
# while j < n:
#     if string[j] in d:
#         d[string[j]] -= 1
#         if d[string[j]] == 0:
#             count -= 1
#     if (j - i + 1) < k:
#         j += 1
#     elif (j - i + 1) == k:
#         if count == 0:
#             ans += 1
#
#         if string[i] in d:
#             d[string[i]] += 1
#             if d[string[i]] == 1:
#                 count += 1
#
#         i += 1
#         j += 1
# print(ans)
#
