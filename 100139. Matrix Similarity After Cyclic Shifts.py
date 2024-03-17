mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2

matIs = [row[:] for row in mat]
for i in mat:
    # print(i)
    k = k % len(i)
    i.extend(i[:k])
    del i[:k]
print(matIs==mat)