


s = "abcabcbb"

sets = set()
i = 0
j = 0
maxLength = 0
while j <len(s):
    if s[j] not in sets:
        sets.add(s[j])
        j += 1
        maxLength = max(maxLength, j - i)
    else:
        sets.remove(s[i])
        i += 1
    # if s[j] in sets:
    #     sets.remove(s[i])
    #     i+=1
    # sets.add(s[j])
    # print(s[i:j],sets)
    # maxLength = max(maxLength,j-i+1)
    # j+=1
print(maxLength)