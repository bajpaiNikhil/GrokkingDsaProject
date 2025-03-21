import heapq

stones = [2,2]
maxHeapStones = [-s for s in stones]
print(maxHeapStones)
heapq.heapify(maxHeapStones)
print(maxHeapStones)
while len(maxHeapStones)>1:
    firstStone = heapq.heappop(maxHeapStones)
    secondStone = heapq.heappop(maxHeapStones)
    if(firstStone != secondStone):
        heapq.heappush(maxHeapStones,-(firstStone-secondStone))
print(maxHeapStones)

# stones = [-s for s in stones]
# heapq.heapify(stones)
#
# while len(stones) > 1:
#     first = -heapq.heappop(stones)
#     second = -heapq.heappop(stones)
#     if first != second:
#         heapq.heappush(stones, -(first - second))
#
# return -stones[0] if stones else 0










# a = []
# for i in stones:
#     a.append(-i)
# print(a)
# heapq.heapify(a)
# print(a)
# while len(a)>1:
#     stoneOne= heapq.heappop(a)
#     stoneTwo = heapq.heappop(a)
#     print(stoneOne,stoneTwo)
#     heapq.heappush(a,-abs(stoneOne-stoneTwo))
# print(-a[0])