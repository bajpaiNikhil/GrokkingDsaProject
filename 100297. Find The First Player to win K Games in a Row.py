skills = [4,2,6,3,9]
k = 2

current = 0

consecutive = 0
for i in range(1,len(skills)):
    if skills[current] > skills[i]:
        consecutive +=1
    else:
        current = i
        consecutive = 1
    if consecutive ==k:
        print(current)
        exit(0)
