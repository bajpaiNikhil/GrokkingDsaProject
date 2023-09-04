from collections import Counter

def differenceCount(s, t):
    char_count1 = Counter(s)
    char_count2 = Counter(t)
    result = []

    #print(char_count1,char_count2)
    unique_characters = []
    for char, count in char_count1.items():
        if char not in char_count2 or count > char_count2[char]:
            unique_characters.extend([char] * (count - char_count2.get(char, 0)))

    return unique_characters

    return result
w = ["xzc", "pcxbcf", "xb", "cxbc", "pcxbc"]
# ['xb', 'xbc', 'cxbc', 'pcxbc', 'pcxbcf']
print(sorted(w, key=len))
w = sorted(w, key=len)
count = 0
pointer1 = 0
maxCount = 0
for i in range(1, len(w)):
    print("hi", w[i], w[pointer1],differenceCount(w[i],w[pointer1]))
    if len(w[i]) - len(w[pointer1]) == 1 and len(differenceCount(w[i],w[pointer1])) == 1:
        count += 1
        print(count, i, pointer1,w[i], w[pointer1], differenceCount(w[i],w[pointer1]))
        pointer1 = i
    else:
        maxCount = max(count, maxCount)
print(maxCount)


def differenceCount(s, t):
    frequency_str1 = Counter(s)
    frequency_str2 = Counter(t)
    result = []

    for key in frequency_str1:
        if key not in frequency_str2:
            result.append(key)
            for key in frequency_str2:
                if key not in frequency_str1:
                    result.append(key)
    return result
