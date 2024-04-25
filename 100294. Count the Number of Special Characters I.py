s = "aaAbcBC"
a = s
a = set(a)

count = 0

for i in s :
    if i.lower() in a and i.upper() in a:
        a.remove(i.lower())
        a.remove(i.upper())
        count += 1

print(count)
