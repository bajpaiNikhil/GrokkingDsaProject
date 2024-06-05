import heapq

ropes = [1, 3, 11, 5]

minHeap = []

for i in ropes:
    heapq.heappush(minHeap, i)
print(minHeap)
returnSum = 0
while len(minHeap) != 1:
    n1 = heapq.heappop(minHeap)
    n2 = heapq.heappop(minHeap)
    returnSum += n1+n2
    heapq.heappush(minHeap,n1+n2)
    print(returnSum,minHeap)
print(returnSum)