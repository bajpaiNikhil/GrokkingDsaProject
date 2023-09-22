import collections

s = "ababbc"
k = 2

longestSubstring = 0
for uniqueCharacter in range(1,27):
    count = collections.Counter()
    left = 0

    for right , c in enumerate(s):
        print(right,c , uniqueCharacter)
        count[c]+=1

        while len(count) > uniqueCharacter:
            print(right, c, count,left, uniqueCharacter)
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left+=1
        print(count)
        if all(t >= k for _, t in count.items()):
            longestSubstring = max(longestSubstring , right-left+1)
print(longestSubstring)