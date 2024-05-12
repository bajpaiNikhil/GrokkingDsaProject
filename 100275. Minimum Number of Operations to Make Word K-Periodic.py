word = "leetcoleet"
k = 2
d = {}
wordIs = ""
wordStart = 1
maxFreq = 0
maxElement = ""
for i in range(len(word)):
    wordIs += word[i]
    if len(wordIs) == k:
        # d.append(wordIs)
        d[wordIs] = d.get(wordIs,0)+1
        if d[wordIs] > maxFreq:
            maxFreq = d[wordIs]
            maxElement = wordIs
        wordIs = ""
# print(d,maxFreq,maxElement)
print(abs(maxFreq-sum(d.values())))

