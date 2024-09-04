# s = "aa"
# t = "aa"
#
# dic = {}
# windowStart = 0
# matched = 0
# min_len = len(s) + 1
# start = 0
# for char in t:
#     dic[char] = dic.get(char, 0) + 1
#
# for i in range(len(s)):
#     if s[i] in dic:
#         dic[s[i]] -= 1
#         if dic[s[i]] == 0:
#             matched += 1
#     # shrinking the window
#     while matched == len(dic):
#         if min_len > i-windowStart+1:
#             min_len = i-windowStart+1
#             start = windowStart
#
#         if s[windowStart] in dic:
#             if dic[s[windowStart]] == 0:
#                 matched-=1
#             dic[s[windowStart]]+=1
#         windowStart+=1
#
# if min_len > len(s):
#     print("")
# print(min_len,start,s[start:start+min_len])
str1 = "azssstaszaztf"
str2 = "saz"
sizeStr1 = len(str1)
sizeStr2 = len(str2)
idxStr1, idxStr2 = 0, 0
start, end = 0, 0
min_Subsequence = ""
length = float("inf")

while idxStr1 < sizeStr1:
    if str1[idxStr1] == str2[idxStr2]:
        idxStr2 += 1
        if idxStr2 == sizeStr2:
            start = idxStr1
            end = idxStr1
            idxStr2-=1
            print(idxStr1,idxStr2,start,end)
            while idxStr2 >= 0:
                if str1[start] == str2[idxStr2]:
                    idxStr2 -= 1
                start -= 1
            start += 1
            if (end - start + 1) < length:
                length = end - start + 1
                min_Subsequence = str1[start:end + 1]
            idxStr1 = start
            idxStr2 = 0
    idxStr1 += 1
print(min_Subsequence)
