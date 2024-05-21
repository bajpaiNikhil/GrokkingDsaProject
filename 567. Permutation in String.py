
s1 ="aa"
s2 ="baa"
patternDic = {}
for char in s1:
    patternDic[char] = patternDic.get(char, 0) + 1
print(patternDic)
matched = 0
windowStart = 0

for j in range(len(s2)):
    if s2[j] in patternDic:
        patternDic[s2[j]] -= 1
        if patternDic[s2[j]] == 0:
            matched += 1
    if matched == len(patternDic):
        print(True)
        print(j,windowStart)
    if j >= len(s1) - 1:
        if s2[windowStart] in patternDic:
            if patternDic[s2[windowStart]] == 0:
                matched -= 1
            patternDic[s2[windowStart]] += 1
        windowStart += 1
print(False)









# import collections
# import math
#
# s = "ab"
# p = "a"
# D = math.inf
# d = {}
# windowStart = 0
# found = 0
#
# for i in p:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
# for i in range(len(s)):
#     if s[i] in d:
#         d[s[i]] -= 1
#         if d[s[i]] == 0:
#             found += 1
#     if found == len(d):
#         print("True")
#         break
#     if i > len(p) - 1:
#         if s[windowStart] in d:
#             if d[s[windowStart]] == 0:
#                 found -= 1
#             d[s[windowStart]] += 1
#         windowStart+=1
# print(False)
#
