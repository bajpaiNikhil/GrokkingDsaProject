

s = "coaching"
t = "coding"

k = s
sPointer = 0
tPointer = 0
while sPointer<=len(s)-1 and tPointer <= len(t)-1:
    if t[tPointer] == s[sPointer]:
        tPointer+=1
        sPointer+=1
    else:
        sPointer+=1
k+=t[tPointer:]
print(k)