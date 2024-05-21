s = "barfoothefoobarman"
words = ["foo", "bar"]

count = {}
wordLength = len(words[0])
wordsLength = wordLength*len(words)
res = []

for i in words:
    count[i] = count.get(i,0)+1
print(count)

for left in range(len(s)-wordsLength+1):

    wordSeen = {}
    for right in range(len(words)):
        wordIndex = left + right*wordLength
        tempWord = s[wordIndex: wordIndex+ wordLength]
        if tempWord not in count :
            break
        wordSeen[tempWord] = wordSeen.get(tempWord,0)+1
        print(tempWord, wordIndex,wordSeen)
        if wordSeen[tempWord]> count[tempWord]:
            break
    if wordSeen == count:
        res.append(left)

print(res)


