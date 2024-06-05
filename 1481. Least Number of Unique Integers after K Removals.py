import heapq

nums = [4,3,1,1,3,3,2]
k = 3

freqHashMap = {}
distinctCount = 0
minHeap = []
for i in nums:
    freqHashMap[i] = freqHashMap.get(i,0)+1
print(freqHashMap)

for key , val in freqHashMap.items():
    heapq.heappush(minHeap,(val , key))
print(minHeap,distinctCount)

while k>0:
    val , key = heapq.heappop(minHeap)
    print("1",minHeap,key,val)
    if val !=1:
        val -=1
        heapq.heappush(minHeap,(val,key))
        print("2",minHeap)
    k-=1

print(minHeap)
