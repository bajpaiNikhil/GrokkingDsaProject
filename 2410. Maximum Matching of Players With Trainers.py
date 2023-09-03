



p = [1,1,1]
t = [10]

p.sort()
t.sort()
pPointer = 0
tPointer = 0
count = 0
while pPointer<=len(p)-1 and tPointer<=len(t)-1:
    if p[pPointer]<t[tPointer]:
        count+=1
        pPointer+=1
        tPointer+=1
    elif p[pPointer]>t[tPointer]:
        tPointer+=1
    else:
        pPointer+=1

print(count)