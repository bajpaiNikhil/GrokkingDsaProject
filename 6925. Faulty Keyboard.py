


s = "string"
k= ""
for i in range(len(s)):
    if s[i] == "i":
        k = k[::-1]
    else:
        k+=s[i]
print(k)

