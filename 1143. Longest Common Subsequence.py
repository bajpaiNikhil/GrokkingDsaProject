def lCS(s, t, indexS, indexT, memo):
    key = f"{indexS},{indexT}"
    if key in memo:
        return memo[key]
    if len(s) == 0 or len(t) == 0:
        return 0
    if indexS == len(s) or indexT == len(t):
        return 0
    if s[indexS] == t[indexT]:
        memo[key] = 1 + lCS(s, t, indexS + 1, indexT + 1, memo)
    else:
        memo[key] = max(lCS(s, t, indexS + 1, indexT, memo),
                        lCS(s, t, indexS, indexT + 1, memo))
    return memo[key]


text1 = "abc"
text2 = "def"
print(lCS(text1, text2, 0, 0, {}))
