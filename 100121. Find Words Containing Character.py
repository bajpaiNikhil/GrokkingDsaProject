words = ["abc","bcd","aaaa","cbc"]
x = "a"
result = []
for i in range(len(words)) :
    if x in words[i]:
        result.append(i)
print(result)