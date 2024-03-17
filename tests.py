n = 6
# queries = [[1, 2, 1009], [3, 3, 5]]
queries = [[1, 2, 4], [2, 2, 8], [1, 1, 4]]
# queries = [[1,1,1],[1,1,42]]
goodArray = []
i = 1
while i <= n:
    if i & n:
        goodArray.append(i)
    i <<= 1
print(goodArray)
k = []
for l,r,m in queries:
    arr = goodArray[l-1:r]
    print(arr,l,r,l-1,m)
    res = 1
    for i in range(l-1,r):
        res = (res*arr[i]) % m
    k.append(res)
print(k)
