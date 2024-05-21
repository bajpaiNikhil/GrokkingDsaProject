

s = "catfoxcat"
p = "catfox"

pDic = {}
windowStart = 0
matched = 0
res = []

for char in p:
    pDic[char] = pDic.get(char,0)+1
print(pDic)
for i in range(len(s)):

    if s[i] in pDic:
        pDic[s[i]] -=1
        if pDic[s[i]] == 0:
            matched+=1
    if matched == len(pDic):
        print(i,windowStart)
        res.append(windowStart)
    if i >= len(p)-1:
        if s[windowStart] in pDic:
            if pDic[s[windowStart]] == 0:
                matched -= 1
            pDic[s[windowStart]] += 1
        windowStart += 1
print(res)





# windowStart = 0
# pCount = {}
# sCount = {}
#
# for i in range(len(p)):
#     pCount[p[i]] = 1 + pCount.get(p[i],0)
#     sCount[s[i]] = 1 + sCount.get(s[i], 0)
# result = [0] if sCount == pCount else []
# print(pCount)
# for windowEnd in range(len(p), len(s)):
#     sCount[s[windowEnd]] = 1 + sCount.get(s[windowEnd],0)
#     sCount[s[windowStart]] -= 1
#     if sCount[s[windowStart]] == 0:
#         sCount.pop(s[windowStart])
#     windowStart+=1
#     if sCount == pCount:
#         result.append(windowStart)
# print(result)




