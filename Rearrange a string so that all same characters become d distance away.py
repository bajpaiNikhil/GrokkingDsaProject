import heapq
from collections import deque

s = "geeksforgeeks"
d = 3

freqHashMap = {}
queue = deque()

if d <= 1:
    print(s)
    exit(0)
for i in s:
    freqHashMap[i] = freqHashMap.get(i, 0) + 1
print(freqHashMap)

maxHeap = []
for key, val in freqHashMap.items():
    heapq.heappush(maxHeap, (-val, key))
print(maxHeap)
result = ""
while maxHeap:
    frequency, key = heapq.heappop(maxHeap)
    result+=key
    queue.append((frequency+1,key))
    if len(queue) == d:
        freq,key = queue.popleft()
        if -freq >0:
            heapq.heappush(maxHeap,(frequency+1,key))
print(result)