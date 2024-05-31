word = "aaaaaaaaaaaaaabb"
wordCountDic = {}


s = ""
i = 0
while i < len(word):
    preLength = 1
    while i+preLength < len(word) and preLength<9 and word[i+preLength] == word[i]:
        preLength+=1
    s+=str(preLength)+word[i]
    i+=preLength
print(s)
