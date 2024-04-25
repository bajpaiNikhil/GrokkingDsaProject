import heapq
import math

points = [[3, 3], [5, -1], [-2, 4]]
k = 2

origin = [0, 0]
distanceHeap = []
for i in points:
    disFromOrigin = -(i[0] ** 2 + i[1] ** 2)
    print(disFromOrigin,distanceHeap)
    if len(distanceHeap) == k:
        heapq.heappushpop(distanceHeap, (disFromOrigin, i))
    else:
        heapq.heappush(distanceHeap, (disFromOrigin, i))
print(distanceHeap)
print([i[1] for i in distanceHeap ])
