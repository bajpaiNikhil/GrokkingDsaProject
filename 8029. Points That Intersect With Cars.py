

s = set()

nums = [[3,6],[1,5],[4,7]]

for i in nums:
    for j in range(i[0],i[1]+1,1):
        s.add(j)


print(len(s))