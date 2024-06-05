import heapq

nums =  [1, 5, 12, 2, 11, 5]
k = 3

minHeap = []
for i in range(k):
    heapq.heappush(minHeap,-nums[i])
print(minHeap)

for i in range(k,len(nums)):
    if -nums[i] > minHeap[0]:
        heapq.heappushpop(minHeap,-nums[i])
print(-minHeap[0])