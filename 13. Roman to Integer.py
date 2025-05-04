

s = "MCMXCIV"

hashMap = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
result = hashMap[s[-1]]

for i in reversed(range(len(s)-1)):
    print(i)
    if hashMap[s[i]] < hashMap[s[i + 1]]:
        result -= hashMap[s[i]]
    else:
        result +=hashMap[s[i]]
print(result)