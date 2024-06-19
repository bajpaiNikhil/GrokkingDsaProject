def wordBreakTwo(s, words, memo):
    result = []
    if len(s) == 0:
        return [[]]
    if s in memo:
        return memo[s]
    for word in words:
        if s[:len(word)] == word:
            suffix = s[len(word):]
            suffixWays = wordBreakTwo(suffix, words, memo)
            # print(suffixWays)
            # result.append(suffixWays)
            for ways in suffixWays:
                # print(word, ways)
                result.append([word] + ways)
    memo[s] = result
    return result


stringIs = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
a = wordBreakTwo(stringIs, wordDict, {})
print(a)
l = []
for words in a:
    l.append(' '.join(words))
print(l)