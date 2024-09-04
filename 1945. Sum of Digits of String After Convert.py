s = "leetcode"
k = 2
convertedString = ""
for char in s:
    convertedString += str(ord(char) - ord("a") + 1)
print(convertedString)

num = sum(int(digit) for digit in convertedString)
print(num)
for _ in range(k - 1):
    num = sum(int(digit) for digit in str(num))

print(num)