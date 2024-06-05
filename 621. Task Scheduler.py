import heapq
from collections import deque

tasks = ["A","A","A","B","B","B"]
n = 2

freqHashMap = {}
maxHeap = []
queue = deque()
intervalCount = 0

for i in tasks:
    freqHashMap[i] = freqHashMap.get(i,0)+1
print(freqHashMap)

for key , val in freqHashMap.items():
    heapq.heappush(maxHeap,(-val,key))
print(maxHeap)
while maxHeap:
    waitList = []
    k = n+1
    while k>0 and maxHeap:
        intervalCount+=1
        freq,key = heapq.heappop(maxHeap)
        if -freq >1 :
            waitList.append((freq+1,key))
        k-=1
    for val,key in waitList:
        heapq.heappush(maxHeap,(val,key))
    if maxHeap:
        intervalCount+=k
print(intervalCount)











