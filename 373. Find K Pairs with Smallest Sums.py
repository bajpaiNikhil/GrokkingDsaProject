import heapq

nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2
heap = []
res = []
visited = set()
heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
print(heap)
visited.add((0,0))
while k >0 and heap:
    currentSum , indxI , indxJ = heapq.heappop(heap)
    res.append([nums1[indxI],nums2[indxJ]])
    if (indxI+1,indxJ) not in visited:
        heapq.heappush(heap,(nums1[indxI+1]+nums2[indxJ], indxI+1,indxJ))
        visited.add((indxI+1,indxJ))
    if (indxI,indxJ+1) not in visited:
        heapq.heappush(heap,(nums1[indxI]+nums2[indxJ+1], indxI,indxJ+1))
        visited.add((indxI,indxJ+1))
    k-=1
print(heap)
print(res)