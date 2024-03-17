s = "abcba"


for i in range(len(s)-1):
    substring = s[i:i+2]
    if substring[::-1] in s:
        print(True)
print(False)