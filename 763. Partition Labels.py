s = "ababcbacadefegdehijhklij"
# d = {}
#
# for i in range(len(s)):
#     if s[i] in d:
#         d[s[i]] = i
#     else:
#         d[s[i]] = i
# d = {s[i]: i for i in range(len(s))}
# print(d)
# # c = {}
# # for j in range(len(s)):
# #     c[s[j]] = j
# # print(c)
# maxRangeOfTheOccurrence = 0
# prev = -1
# result = []
# for i in range(len(s)):
#     characterAt = s[i]
#     maxRangeOfTheOccurrence = max(maxRangeOfTheOccurrence,d[characterAt])
#     print(characterAt,maxRangeOfTheOccurrence,i)
#     if maxRangeOfTheOccurrence == i:
#         result.append(maxRangeOfTheOccurrence-prev)
#         prev = maxRangeOfTheOccurrence
# print(result)


lastIndexHashMap = {s[i]: i for i in range(len(s))}
print(lastIndexHashMap)
maxRangeOfCharacter = 0
previousRangeOfCharacter = -1
result = []
for i in range(len(s)):
    maxRangeOfCharacter = max(maxRangeOfCharacter, lastIndexHashMap[s[i]])
    print(maxRangeOfCharacter, lastIndexHashMap[s[i]])
    if maxRangeOfCharacter == i:
        result.append(maxRangeOfCharacter - previousRangeOfCharacter)
        previousRangeOfCharacter = maxRangeOfCharacter
print(result)
