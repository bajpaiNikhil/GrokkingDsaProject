import heapq

nums = [1, 3, 12, 5, 15, 11]
K1=3
K2=6
minHeap = []
for i in nums:
    heapq.heappush(minHeap,i)
print(minHeap)
i = 0
while i<K1:
    heapq.heappop(minHeap)
    i+=1
print(minHeap)
elementSum = 0
for _ in range(K2-K1-1):
    # print(_)
    elementSum+=heapq.heappop(minHeap)
print(elementSum)
