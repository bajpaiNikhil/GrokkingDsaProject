import heapq

stones = [2,2]
a = []
for i in stones:
    a.append(-i)
print(a)
heapq.heapify(a)
print(a)
while len(a)>1:
    stoneOne= heapq.heappop(a)
    stoneTwo = heapq.heappop(a)
    heapq.heappush(a,-abs(stoneOne-stoneTwo))
print(-a[0])