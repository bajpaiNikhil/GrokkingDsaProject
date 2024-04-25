s = "aaAbcBC"
uniqueSet = set(s)

count = 0

for i in s:

    if i.lower() in uniqueSet and i.upper() in uniqueSet:
        if s.rindex(i.lower()) < s.index(i.upper()):
            uniqueSet.remove(i.lower())
            uniqueSet.remove(i.upper())
            count += 1

print(count)
word = "aaAbcBC"
w = word.lower()
w = list(set(w))
s = 0
for i in w:
    if i.upper() in word and i.lower() in word and word.index(i.upper()) > word.rindex(i.lower()):
        s += 1

print(s)
